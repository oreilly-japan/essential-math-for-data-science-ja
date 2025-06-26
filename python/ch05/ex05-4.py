# 例5-4 直線とデータに対する二乗和を求める例

import pandas as pd

# 点を読み込む
points = pd.read_csv("https://bit.ly/2KF29Bd").itertuples()

# 直線を与える
m = 1.93939
b = 4.73333

sum_of_squares = 0.0

# 二乗和を求める
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual_squared = (y_predict - y_actual)**2
    sum_of_squares += residual_squared

print("sum of squares = {}".format(sum_of_squares))
