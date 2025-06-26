# 例5-7 QR分解を使って線形回帰を実行する例

import pandas as pd
from numpy.linalg import qr, inv
import numpy as np

# 点を読み込む
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
X = df.values[:, :-1].flatten()

# 「1」のプレースホルダー列を追加し、切片を生成する
X_1 = np.vstack([X, np.ones(len(X))]).transpose()

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# QR分解を使って傾きと切片の係数を求める
Q, R = qr(X_1)
b = inv(R).dot(Q.transpose()).dot(Y)

print(b)
