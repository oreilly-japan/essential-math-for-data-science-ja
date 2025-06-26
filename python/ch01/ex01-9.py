# 例1-9 Pythonで2つの独立変数を使った関数を定義する例

from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)