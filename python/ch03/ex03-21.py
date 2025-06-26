# 例3-21 統計的有意性が5%となる範囲を求める例

from scipy.stats import norm

# 風邪の平均回復期間は18日、標準偏差は1.5日とする
mean = 18
std_dev = 1.5

# 2.5%の面積のx値
x1 = norm.ppf(0.025, mean, std_dev)

# 97.5%の面積のx値
x2 = norm.ppf(0.975, mean, std_dev)

print(x1)
print(x2)
