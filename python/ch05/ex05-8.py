# 例5-8 勾配降下法を使って放物線の最小値を見つける例

import random

def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2*(x - 3)

# 学習率
L = 0.001

# 勾配降下法を実行する反復回数
iterations = 100_000

 # ランダムなxの値を使って開始する
x = random.randint(-15,15)

for i in range(iterations):

    # 傾きを得る
    d_x = dx_f(x)

    # 学習率と傾きを掛けた値を引いてxの値を更新する
    x -= L * d_x

print(x, f(x))
