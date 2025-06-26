# A-10 ヒルクライミング法を使ったシンプルなロジスティック回帰

import math
import random

import numpy as np
import pandas as pd


# Desmosのグラフ https://www.desmos.com/calculator/6cb10atg3l

points = [p for p in pd.read_csv("https://tinyurl.com/y2cocoo7").itertuples()]

best_likelihood = -10_000_000
b0 = 0.01
b1 = 0.01


# 最尤推定を求める
def predict_probability(x):
    p = 1.0 / (1.0001 + math.exp(-(b0 + b1 * x)))
    return p


for i in range(1_000_000):

    # b0やb1をランダムに選択、調整する
    random_b = random.choice(range(2))

    random_adjust = np.random.normal()

    if random_b == 0:
        b0 += random_adjust
    elif random_b == 1:
        b1 += random_adjust

    # 尤度の合計を求める
    true_estimates = sum(math.log(predict_probability(p.x)) \
        for p in points if p.y == 1.0)
    false_estimates = sum(math.log(1.0 - predict_probability(p.x)) \
        for p in points if p.y == 0.0)

    total_likelihood = true_estimates + false_estimates

    # 尤度が改善される場合は、その調整値を採用する。改善されない場合は破棄する
    if best_likelihood < total_likelihood:
        best_likelihood = total_likelihood
    elif random_b == 0:
        b0 -= random_adjust
    elif random_b == 1:
        b1 -= random_adjust

print("1.0 / (1 + exp(-({0} + {1}*x)))".format(b0, b1))
print("BEST LIKELIHOOD: {:.6f}".format(math.exp(best_likelihood)))
