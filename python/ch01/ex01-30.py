# 例1-30 極限を使って積分する例

from sympy import *

# SymPyで変数を定義する
x, i, n = symbols('x i n')

# 関数を宣言し、範囲を定義する
f = x**2 + 1
lower, upper = 0, 1

# 幅と、インデックスiの長方形の高さを求める
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# n個の長方形について繰り返し、その面積を合計する
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# 長方形の個数nを無限大に近づけて、面積を求める
area = limit(n_rectangles, n, oo)

print(area)
