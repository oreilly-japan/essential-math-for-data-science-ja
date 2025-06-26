# 例6-1 独立変数がひとつのロジスティック関数をPythonで定義した例

import math

def predict_probability(x, b0, b1):
    p = 1.0 / (1.0 + math.exp(-(b0 + b1 * x)))
    return p
