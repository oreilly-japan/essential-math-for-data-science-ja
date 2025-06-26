# 演習2-4

from scipy.stats import binom

n = 137
p = 0.40

p_50_or_more_noshows = 0.0

for x in range(50,138):
    p_50_or_more_noshows += binom.pmf(x, n, p)

print(p_50_or_more_noshows)
