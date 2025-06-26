# 例1-21 SymPyで偏微分を求める例

from sympy import *
from sympy.plotting import plot3d

# SymPyでxとyを定義する
x,y = symbols('x y')

# Pythonの構文で関数を宣言する
f = 2*x**3 + 3*y**3

# xとyの偏微分を求める
dx_f = diff(f, x)
dy_f = diff(f, y)

print(dx_f) # 6*x**2と出力される
print(dy_f) # 9*y**2と出力される

# 関数を描画する
plot3d(f)
