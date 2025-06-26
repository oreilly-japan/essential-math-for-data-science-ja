# 例5-19 推定標準誤差を求める例

import pandas as pd
from math import sqrt

# データを読み込む
points = list(pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",").itertuples())

n = len(points)

# 回帰直線の値を定義する
m = 1.939
b = 4.733

# 推定標準誤差を求める
S_e = sqrt((sum((p.y - (m*p.x +b))**2 for p in points))/(n-2))

print(S_e)
