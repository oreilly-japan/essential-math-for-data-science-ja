# 例6-17 scikit-learnでテスト用データセットの混同行列を生成する例

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# データを読み込む
df = pd.read_csv('https://bit.ly/3cManTi', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33,
    random_state=10)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

"""
混同行列は、それぞれの観点で精度を評価する。
[[TP（真陽性） FN（偽陰性）]
 [FP（偽陽性） TN（真陰性）]]

左上から右下の対角線上の値は、予測が正しいことを示すため、
高いほどよい。
"""
matrix = confusion_matrix(y_true=Y_test, y_pred=prediction)
print(matrix)