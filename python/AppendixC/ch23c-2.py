# 例C-2 データの相関係数とp値を求める例

import numpy as np
import pandas as pd

# アイスクリームの売上（万円）
ice_cream_sales = [189, 191, 203, 349,
                   468, 508, 617, 653,
                   550, 404, 302, 226]
# 犯罪件数（件）
crime_rate = [901, 1031, 1111, 1272,
              1343, 1526, 1714, 1646,
              1451, 1252, 1173, 1129]

# データフレームを作成
df = pd.DataFrame({
    "IceCreamSales": ice_cream_sales,
    "CrimeRate": crime_rate
})

# 相関行列を確認
correlation_matrix = df.corr()
print(correlation_matrix)

# 相関係数とp値を求める
n = len(df)

from scipy import stats

correlation = np.corrcoef(df["IceCreamSales"], df["CrimeRate"])[0, 1]
t = correlation * np.sqrt((n - 2) / (1 - correlation ** 2))

if t > 0:
    p_value = 1.0 - stats.t(n - 2).cdf(t)
else:
    p_value = t(n - 2).cdf(t)

# 両側検定のため、2を掛ける
p_value = p_value * 2

# 結果を表示
print(f"相関係数: {correlation:.06f}")
print(f"p値: {p_value:.10f}")
