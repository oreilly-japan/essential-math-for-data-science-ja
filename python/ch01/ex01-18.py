# 例1-18 SymPyで導関数を求める例

from sympy import *

# SymPyで'x'を定義する
x = symbols('x')

# Pythonの構文で関数を宣言する
f = x**2

# この関数の導関数を求める
dx_f = diff(f)
print(dx_f)