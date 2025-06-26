# 例1-16 SymPyを使って極限を求める例

from sympy import *

x = symbols('x')
f = 1 / x
result = limit(f, x, oo)

print(result)
