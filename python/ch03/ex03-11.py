# 例3-11 中間部分の範囲の確率をCDFを使って求める例

from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.cdf(66, mean, std_dev) - norm.cdf(62, mean, std_dev)

print(x)
