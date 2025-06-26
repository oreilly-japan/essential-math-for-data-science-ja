# 例1-13 Pythonで月ごとに福利計算する例

p = 100
r = 0.20
t = 2.0
n = 12

a = p * (1 + (r/n))**(n * t)
print(a)
