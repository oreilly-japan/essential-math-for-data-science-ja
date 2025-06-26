# 例3-22 両側検定のp値を求める例

from scipy.stats import norm

# 風邪の平均回復期間は18日、標準偏差は1.5日とする
mean = 18
std_dev = 1.5

# 16日以下の確率
p1 = norm.cdf(16, mean, std_dev)

# 20日以上の確率
p2 = 1.0 - norm.cdf(20, mean, std_dev)

# 両側のp値
p_value = p1 + p2
print(p_value)
