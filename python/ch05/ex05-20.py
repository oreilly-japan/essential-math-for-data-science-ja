# 例5-20 8.5歳の犬に対する動物病院への通院回数の予測区間を求める例

import pandas as pd
from scipy.stats import t
from math import sqrt

# データを読み込む
points = list(pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",").itertuples())

n = len(points)

# 線形回帰直線
m = 1.939
b = 4.733

# x = 8.5に対する予測区間を求める
x_0 = 8.5
x_mean = sum(p.x for p in points) / len(points)

t_value = t(n - 2).ppf(0.975)

standard_error = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in points) / (n - 2))

margin_of_error = t_value * standard_error * \
                  sqrt(1 + (1 / n) + (n * (x_0 - x_mean) ** 2) / \
                       (n * sum(p.x ** 2 for p in points) - \
                            sum(p.x for p in points) ** 2))

predicted_y = m*x_0 + b

# 予測区間の計算
print(predicted_y - margin_of_error, predicted_y + margin_of_error)
