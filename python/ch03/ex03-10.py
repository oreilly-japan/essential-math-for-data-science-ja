# 例3-10 Pythonでの正規分布のCDFの例

from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.cdf(64.43, mean, std_dev)

print(x)
