# 演習1-6

from math import exp

p = 1000 # 元本、開始時の金額
r = 0.05 # 年ごとの金利
t = 3.0 # 年数

a = p * exp(r*t)

print(a)
