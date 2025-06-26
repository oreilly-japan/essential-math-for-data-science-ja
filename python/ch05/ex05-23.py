# 例5-23 線形回帰にランダムフォールド検証を使う例

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, ShuffleSplit

df = pd.read_csv('https://bit.ly/38XwbeB', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 単純な線形回帰（単回帰）を実行する
kfold = ShuffleSplit(n_splits=10, test_size=0.33, random_state=7)
model = LinearRegression()
results = cross_val_score(model, X, Y, cv=kfold)

print(results)
print("mean=%.3f (stdev-%.3f)" % (results.mean(), results.std()))
