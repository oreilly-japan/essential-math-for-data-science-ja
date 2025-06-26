# 例C-3 偏相関係数とp値を求める例


import numpy as np
import pandas as pd

temperature = [5, 6, 10, 15,
               20, 24, 28, 30,
               25, 18, 12, 7]
ice_cream_sales = [189, 191, 203, 349,
                   468, 508, 617, 653,
                   550, 404, 302, 226]
crime_rate = [901, 1031, 1111, 1272,
              1343, 1526, 1714, 1646,
              1451, 1252, 1173, 1129]

df = pd.DataFrame({
    "Temperature": temperature,
    "IceCreamSales": ice_cream_sales,
    "CrimeRate": crime_rate
})

# 偏相関係数の定義（3変数）
def compute_partial_correlation(x, y, z):
    r_xy = np.corrcoef(x, y)[0, 1]
    r_xz = np.corrcoef(x, z)[0, 1]
    r_yz = np.corrcoef(y, z)[0, 1]
    numerator = r_xy - r_xz * r_yz
    denominator = np.sqrt((1 - r_xz ** 2) * (1 - r_yz ** 2))
    return numerator / denominator

# Temperatureの影響を除去した
# IceCreamSalesとCrimeRateの偏相関係数を求める
partial_corr_result = compute_partial_correlation(
    df["IceCreamSales"],
    df["CrimeRate"],
    df["Temperature"]
)

# p値を求める
n = len(df)

# 統計量を求める（自由度 n - 3）
t = partial_corr_result * np.sqrt((n - 3) / (1 - partial_corr_result**2))

from scipy import stats

if t > 0:
    p_value = 1.0 - stats.t(n - 2).cdf(t)
else:
    p_value = t(n - 2).cdf(t)

# 両側検定のため、2を掛ける
p_value = p_value * 2

# 結果を表示
print(f"偏相関係数: {partial_corr_result:.03f}")
print(f"p値: {p_value:.03f}")
