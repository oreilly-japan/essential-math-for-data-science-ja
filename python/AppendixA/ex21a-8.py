# A-8 時間経過に伴う漏れの発生確率を予測するコードの例

from math import exp

# 1年あたりの漏れの確率
p_leak = 0.05

# 年数
t = 5

# 5年以内に漏れが生じる確率
p_leak_5_years = 1.0 - exp(-p_leak * t)

print("PROBABILITY OF LEAK WITHIN 5 YEARS: {}".format(p_leak_5_years))
