# 例5-6 逆行列と転置行列を使って線形回帰を当てはめる例

import pandas as pd
from numpy.linalg import inv
import numpy as np

# 点を読み込む
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1].flatten()

# 「1」のプレースホルダー列を追加し、切片を生成する
X_1 = np.vstack([X, np.ones(len(X))]).T

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 傾きと切片の係数を求める
b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(b) # [1.93939394, 4.73333333]

print(X_1)
# yの値を予測する
y_predict = X_1.dot(b)
print(y_predict)
