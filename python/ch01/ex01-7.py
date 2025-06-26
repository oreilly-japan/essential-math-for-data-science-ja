# 例1-7 SymPyを使ってPythonで一次関数を描画する例

from sympy import *

x = symbols('x')
f = 2*x + 1
plot(f)