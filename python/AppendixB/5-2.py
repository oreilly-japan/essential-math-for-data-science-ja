# 演習5-2

import pandas as pd

# データをPandasのデータフレームとして読み込む
df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",")

# 変数間の相関係数を求め、二乗して表示する
correlations = df.corr(method='pearson')
print(correlations)

# 出力:
#          x        y
# x  1.00000  0.92421
# y  0.92421  1.00000

# 統計的有意性を確かめる
from scipy.stats import t
from math import sqrt

# 標本のサイズ
n = df.shape[0]
print(n)
lower_cv = t(n - 1).ppf(0.025)
upper_cv = t(n - 1).ppf(0.975)

# 相関係数を求める
r = correlations["y"]["x"]

# 検定を実行する
test_value = r / sqrt((1 - r ** 2) / (n - 2))

print("TEST VALUE: {}".format(test_value))
print("CRITICAL RANGE: {}, {}".format(lower_cv, upper_cv))

if test_value < lower_cv or test_value > upper_cv:
    print("CORRELATION PROVEN, REJECT H0")
else:
    print("CORRELATION NOT PROVEN, FAILED TO REJECT H0 ")

# p値を求める
if test_value > 0:
    p_value = 1.0 - t(n - 1).cdf(test_value)
else:
    p_value = t(n - 1).cdf(test_value)

# 両側検定のため結果を2倍する
p_value = p_value * 2
print("P-VALUE: {}".format(p_value))
