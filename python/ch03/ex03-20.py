# 例3-20 片側検定のp値を求める例

from scipy.stats import norm

# 風邪の平均回復期間は18日、標準偏差は1.5日とする
mean = 18
std_dev = 1.5

# 16日以下となる確率
p_value = norm.cdf(16, mean, std_dev)
print(p_value)
