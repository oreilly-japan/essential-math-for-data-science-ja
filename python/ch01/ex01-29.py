# 例1-29 SymPyで積分する例

from sympy import *

# SymPyで'x'を定義する
x = symbols('x')

# Pythonの構文で関数を宣言する
f = x**2 + 1

# 関数をxについて積分し、x = 0から1の範囲の面積を求める
area = integrate(f, (x, 0, 1))

print(area)
