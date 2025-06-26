# 例3-12 Pythonで【ppf()】関数を呼び出してICDFを使う例

from scipy.stats import norm

x = norm.ppf(0.95, loc=64.43, scale=2.99)
print(x)
