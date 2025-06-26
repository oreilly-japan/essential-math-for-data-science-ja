# 演習2-5

from scipy.stats import beta

heads = 8
tails = 2

p = 1.0 - beta.cdf(0.5, heads, tails)

print(p)
