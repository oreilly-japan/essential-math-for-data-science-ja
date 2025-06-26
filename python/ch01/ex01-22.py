# 例1-22 極限を使って傾きを求める例

from sympy import *

# xと、傾きsを定義する
x, s = symbols('x s')

# 関数を宣言する
f = x**2

# 傾きの公式に代入して、
# sだけ離れた2点間の傾きを求める
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# xに2を代入する
slope_2 = slope_f.subs(x, 2)

# x = 2のときの傾きを求める
# 間隔_s_を限りなく0に近づける
result = limit(slope_2, s, 0)

print(result)