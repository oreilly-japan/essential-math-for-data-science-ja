# 例1-25 連鎖律の有無にかかわらず同じ導関数dz/dxが得られる例

from sympy import *

x, y = symbols('x y')


# 1つ目の関数の導関数
# 変数の衝突を避けるために yの前にアンダースコアを付ける
_y = x**2 + 1
dy_dx = diff(_y)

# 2つ目の関数の導関数
z = y**3 - 2
dz_dy = diff(z)

# 連鎖律を使って求めた導関数と、yを代入して直接求めた導関数
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# 両者が等しいことを示し、連鎖律を証明
print(dz_dx_chain)
print(dz_dx_no_chain)
