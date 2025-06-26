# 例5-24 ふたつの入力変数がある線形回帰の例

import pandas as pd
from sklearn.linear_model import LinearRegression

# データを読み込む
df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 訓練する
fit = LinearRegression().fit(X, Y)

# 相関を表示する
print("Coefficients = {0}".format(fit.coef_))
print("Intercept = {0}".format(fit.intercept_))
print("z = {0} + {1}x + {2}y".format(fit.intercept_, fit.coef_[0], fit.coef_[1]))
