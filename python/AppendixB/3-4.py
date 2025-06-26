# 演習3-4

from scipy.stats import norm

mean = 10345
std_dev = 552

p1 = 1.0 - norm.cdf(11641, mean, std_dev)

# 対称性を利用する
p2 = p1

# 両側のp値
# 単純に値を2倍するだけでも求められる
p_value = p1 + p2

print("Two-tailed P-value", p_value)
if p_value <= 0.05:
    print("Passes two-tailed test")
else:
    print("Fails two-tailed test")
