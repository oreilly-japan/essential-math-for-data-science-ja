# 演習1-8

from sympy import *

# SymPyで'x'を定義する
x = symbols('x')

# Pythonの構文で関数を宣言する
f = 3*x**2 + 1

# 関数をxについて積分し、x = 0から2の範囲の面積を求める
area = integrate(f, (x, 0, 2))

print(area)
