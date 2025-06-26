# 例5-13 線形回帰に確率的勾配降下法を使った例

import pandas as pd
import numpy as np

# 入力データ
data = pd.read_csv('https://bit.ly/2KF29Bd', header=0)

X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values

n = data.shape[0]  # 行数

# モデルを構築する
m = 0.0
b = 0.0

sample_size = 1  # 標本のサイズ
L = 0.0001  # 学習率
epochs = 1_000_000  # 勾配降下法を実行する反復の回数

# 確率的勾配降下法を実行する
for i in range(epochs):
    idx = np.random.choice(n, sample_size, replace=False)
    x_sample = X[idx]
    y_sample = Y[idx]

    # 現在のyの予測値
    Y_pred = m * x_sample + b

    # 損失関数をmで偏微分する
    D_m = (-2 / sample_size) * sum(x_sample * (y_sample - Y_pred))

    # 損失関数をbで偏微分する
    D_b = (-2 / sample_size) * sum(y_sample - Y_pred)
    m = m - L * D_m  # mを更新する
    b = b - L * D_b  # bを更新する

    # 進捗を表示する
    if i % 10000 == 0:
        print(i, m, b)

print("y = {0}x + {1}".format(m, b))
