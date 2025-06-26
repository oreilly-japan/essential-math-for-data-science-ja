# 例5-18 Pandasで相関行列を生成する例

import pandas as pd

# データをPandasのデータフレームとして読み込む
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# 変数間の相関係数を求め、二乗して表示する
coeff_determination = df.corr(method='pearson') ** 2
print(coeff_determination)
