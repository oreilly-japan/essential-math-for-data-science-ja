# 例5-17 線形に見えるデータの優位性を検定する例

from scipy.stats import t
from math import sqrt

# 標本のサイズ
n = 10

lower_cv = t(n-1).ppf(0.025)
upper_cv = t(n-1).ppf(0.975)

# https://bit.ly/2KF29Bd のデータから求めた相関係数
r = 0.957586

# 検定を実行する
test_value = r / sqrt((1-r**2) / (n-2))

print("TEST VALUE: {}".format(test_value))
print("CRITICAL RANGE: {}, {}".format(lower_cv, upper_cv))

if test_value < lower_cv or test_value > upper_cv:
    print("CORRELATION PROVEN, REJECT H0")
else:
    print("CORRELATION NOT PROVEN, FAILED TO REJECT H0 ")

# p値を求める
if test_value > 0:
    p_value = 1.0 - t(n-1).cdf(test_value)
else:
    p_value = t(n-1).cdf(test_value)

# 両側検定のため、2を掛ける
p_value = p_value * 2
print("P-VALUE: {}".format(p_value))
