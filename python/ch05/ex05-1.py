# 例5-1 scikit-learnを使って線形回帰を実行する例

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# データを読み込む
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1]

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 点を直線に当てはめる
fit = LinearRegression().fit(X, Y)

# m = 1.7867224, b = -16.51923513
m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# グラフを表示する
plt.plot(X, Y, 'o') # 点
plt.plot(X, m*X+b) # 直線
plt.show()
