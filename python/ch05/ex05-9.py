# 例5-9 線形回帰における勾配降下法の実行例

import pandas as pd

# CSVから点を読み込む
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# モデルを構築する
m = 0.0
b = 0.0


# 学習率
L = 0.001

# 反復の回数
iterations = 100_000

n = float(len(points))  # Xの要素数

# 勾配降下法を実行する
for i in range(iterations):

    # mに対する傾き
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points)

    # bに対する傾き
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in points)

    # mとbを更新する
    m -= L * D_m
    b -= L * D_b

print("y = {0}x + {1}".format(m, b))
