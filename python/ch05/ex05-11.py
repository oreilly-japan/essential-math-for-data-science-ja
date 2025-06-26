# 例5-11 SymPyを使って線形回帰を実行する例

import pandas as pd
from sympy import *

# CSVから点を読み込む
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

d_m = diff(sum_of_squares, m) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

d_b = diff(sum_of_squares, b) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# lambdifyを使ってラムダ関数に変換し高速に計算できるようにする
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# モデルの構築
m = 0.0
b = 0.0

# 学習率
L = 0.001

# 反復の回数
iterations = 100_000

# 勾配降下法を実行する
for i in range(iterations):

    # mとbを更新する
    m -= d_m(m,b) * L
    b -= d_b(m,b) * L

print("y = {0}x + {1}".format(m, b))
