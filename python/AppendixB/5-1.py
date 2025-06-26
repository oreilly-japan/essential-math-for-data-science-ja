# 演習5-1

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# データを読み込む
df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# データに直線を当てはめる
fit = LinearRegression().fit(X, Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# チャートを表示する
plt.plot(X, Y, 'o') # 散布図
plt.plot(X, m*X+b) # 直線
plt.show()
