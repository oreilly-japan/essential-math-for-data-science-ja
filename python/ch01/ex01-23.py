# 例1-23 極限を使って導関数を求める例

from sympy import *

# xと、傾きsを定義する
x, s = symbols('x s')

# 関数を宣言する
f = x**2

# 傾きの公式に代入して、
# sだけ離れた2点間の傾きを求める
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# 導関数を求める
# 間隔_s_を限りなく0に近づける
result = limit(slope_f, s, 0)

print(result)
