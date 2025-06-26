# 例3-19 5%の面積に対応するx値を得る例

from scipy.stats import norm

# 風邪の平均回復期間は18日、標準偏差は1.5日とする
mean = 18
std_dev = 1.5

# 5%の面積に対応するx値を得る
x = norm.ppf(0.05, mean, std_dev)

print(x)
