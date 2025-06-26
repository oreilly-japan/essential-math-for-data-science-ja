# A-9 線形回帰にヒルクライミング法を使う例

from numpy.random import normal
import pandas as pd

# CSVから点を読み込む
points = [p for p in pd.read_csv("https://bit.ly/2KF29Bd").itertuples()]

# モデルを構築する
m = 0.0
b = 0.0

#実行する反復の数
iterations = 1000000

# 点の個数
n = float(len(points))

# 損失の初期値に極めて大きな値を設定する
# この値は反復処理で更新される
best_loss = 10000000000000.0

for i in range(iterations):

    # 「m」と「b」をランダムに調整する
    m_adjust = normal(0,1)
    b_adjust = normal(0,1)

    m += m_adjust
    b += b_adjust

    # 損失（二乗和誤差の合計）を求める
    new_loss = 0.0
    for p in points:
        new_loss += (p.y - (m * p.x + b)) ** 2

    # 損失が改善された場合はその値を採用し、そうでない場合は破棄する
    if new_loss < best_loss:
        print("y = {0}x + {1}".format(m, b))
        best_loss = new_loss
    else:
        m -= m_adjust
        b -= b_adjust

print("y = {0}x + {1}".format(m, b))