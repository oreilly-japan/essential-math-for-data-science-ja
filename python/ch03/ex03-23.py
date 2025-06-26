# 例3-23 t分布で臨界値範囲を求める例

from scipy.stats import t

# 標本のサイズが25のときの
# 95%信頼区間の臨界値範囲を得る

n = 25
lower = t.ppf(0.025, df=n-1)
upper = t.ppf(0.975, df=n-1)

print(lower, upper)
