# 例6-8 ロジスティック回帰に勾配降下法を使う例

from sympy import *
import pandas as pd

points = list(pd.read_csv("https://tinyurl.com/y2cocoo7").itertuples())

b1, b0, i, n = symbols('b1 b0 i n')
x, y = symbols('x y', cls=Function)
joint_likelihood = Sum(log((1.0 / (1.0 + exp(-(b0 + b1 * x(i))))) ** y(i) \
    * (1.0 - (1.0 / (1.0 + exp(-(b0 + b1 * x(i)))))) ** (1 - y(i))), (i, 0, n))

# データの点を代入し、beta1（傾き）の偏微分を求める
d_b1 = diff(joint_likelihood, b1) \
           .subs(n, len(points) - 1).doit() \
           .replace(x, lambda i: points[i].x) \
           .replace(y, lambda i: points[i].y)

# データの点を代入し、beta0（切片）の偏微分を求める
d_b0 = diff(joint_likelihood, b0) \
           .subs(n, len(points) - 1).doit() \
           .replace(x, lambda i: points[i].x) \
           .replace(y, lambda i: points[i].y)

# lambdify関数でコンパイルして計算を高速化する
d_b1 = lambdify([b1, b0], d_b1)
d_b0 = lambdify([b1, b0], d_b0)

# 勾配降下法を実行する
b1 = 0.01
b0 = 0.01
L = 0.01

for j in range(10_000):
    b1 += d_b1(b1, b0) * L
    b0 += d_b0(b1, b0) * L

print(b1, b0)
