# 演習1-7

from sympy import *

# SymPyで'x'を定義する
x = symbols('x')

# Pythonの構文で関数を宣言する
f = 3*x**2 + 1

# この関数の導関数を求める
dx_f = diff(f)
print(dx_f)
print(dx_f.subs(x,3))
