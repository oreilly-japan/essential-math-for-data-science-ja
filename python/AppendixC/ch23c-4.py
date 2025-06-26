# 例C-4 偏相関係数とp値をライブラリを使って求める例
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

import pingouin as pg

# 偏相関係数やp値を求める
partial_corr_result = pg.partial_corr(data=df, x='IceCreamSales', y='CrimeRate', covar='Temperature')
partial_corr = partial_corr_result["r"][0]
p_value = partial_corr_result["p-val"][0]

# 結果を表示
print(f"偏相関係数: {partial_corr:.03f}")
print(f"p値: {p_value:.03f}")

