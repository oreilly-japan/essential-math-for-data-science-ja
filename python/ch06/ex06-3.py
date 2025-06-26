# 例6-3 scikit-learnで基本的なロジスティック回帰を実行する例

import pandas as pd
from sklearn.linear_model import LogisticRegression

# データを読み込む
df = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# ロジスティック回帰を実行する
# （ペナルティをNone）
model = LogisticRegression(penalty=None)
model.fit(X, Y)

# beta1を表示する
print(model.coef_.flatten())

# beta0を表示する
print(model.intercept_.flatten())
