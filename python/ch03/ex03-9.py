# 例3-9 正規分布の確率密度関数のPythonでの実装例

import math


# xにおける正規分布の確率密度を返す
def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * \
        math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))