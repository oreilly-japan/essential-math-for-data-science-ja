# 例3-18 15日から21日の間に回復する確率を求める例

from scipy.stats import norm

# 風邪の平均回復期間は18日、標準偏差は1.5日とする
mean = 18
std_dev = 1.5

# 回復期間が15日から21日の範囲に収まる確率は95%となる
x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)

print(x)
