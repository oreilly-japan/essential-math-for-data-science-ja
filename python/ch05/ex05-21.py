# 例5-21 線形回帰のデータを訓練用データとテスト用データに分割する例

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# データを読み込む
df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 訓練用とテスト用にデータを分割する
# これによりデータの1/3がテスト用になる
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

model = LinearRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("r^2: %.3f" % result)
