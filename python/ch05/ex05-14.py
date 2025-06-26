# 例5-14 Pandasを使って変数の組み合わせに対する相関係数を確認する例

import pandas as pd

# データをPandasのデータフレームとして読み込む
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# 変数間の相関係数を出力する
correlations = df.corr(method='pearson')
print(correlations)
