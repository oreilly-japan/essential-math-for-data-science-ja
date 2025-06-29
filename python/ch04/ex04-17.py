# 例4-17 SymPyを使って逆行列と単位行列を確認する例

from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# 行列Aとその逆行列の行列積を取り、
# 単位行列を得る
inverse = A.inv()
identity = inverse * A

print("INVERSE: {}".format(inverse))
print("IDENTITY: {}".format(identity))
