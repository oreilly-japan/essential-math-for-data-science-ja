# 演習4-6 別解
# SymPyを使えば、浮動小数点の誤差を回避して正確に0が得られます。

from sympy import *

basis = Matrix([
    [2,1],
    [6,3]
])

determinant = det(basis)

print(determinant)
