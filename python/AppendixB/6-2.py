# 演習6-2

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# データを読み込む
df = pd.read_csv("https://bit.ly/3imidqa", delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

"""
混同行列は、カテゴリごとの予測の精度を評価するものです。
[[真陽性（True Positives）  偽陰性（False Negatives）]
 [偽陽性（False Positives） 真陰性（True Negatives）]]
この行列の左上から右下の対角線上の値は正しい予測を表しており、
これらの値が大きいほどよい結果になります。
"""
matrix = confusion_matrix(y_true=Y_test, y_pred=prediction)
print(matrix)
