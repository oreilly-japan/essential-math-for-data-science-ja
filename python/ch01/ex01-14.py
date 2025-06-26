# 例1-14 Pythonで連続的な複利計算を行う例

from math import exp

p = 100 # 元本、開始時の金額
r = 0.20 # 年ごとの金利
t = 2.0 # 年数

a = p * exp(r*t)

print(a)
