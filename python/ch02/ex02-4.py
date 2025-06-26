# 例2-4 ベータ分布で求めた面積を引き算する例

from scipy.stats import beta

a = 8
b = 2

p = 1.0 - beta.cdf(0.90, a, b)
print(p)
