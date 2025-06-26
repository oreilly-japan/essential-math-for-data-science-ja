# 例C-5 gcastleを使って因果探索を行う例
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
data = df.values.astype(float)
cols = df.columns.tolist()

from castle.algorithms import Notears

# NOTEARSアルゴリズムによって因果行列（因果関係の行列）を求める
notears = Notears()
notears.learn(data=df.values, columns=df.columns)
print(notears.causal_matrix)
