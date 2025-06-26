# コラム SymPyによる式の簡略化

from sympy import *

x = symbols('x')
expr = x**2 / x**5
print(expr)
