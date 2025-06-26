# A-1 SymPyを使って数式をLaTeX形式に変換する例

from sympy import *

x,y = symbols('x y')

z = x**2 / sqrt(2*y**3 - 1)

print(latex(z))
