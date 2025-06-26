# 例5-2 直線とデータとの残差を求める例

import pandas as pd

# 点を読み込む
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()

# 直線を与える
m = 1.93939
b = 4.73333

# 残差を求める
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual = y_actual - y_predict
    print(residual)
