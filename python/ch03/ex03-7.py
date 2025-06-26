# 例3-7 Pythonで標準偏差を求める例

from math import sqrt

# 飼っているペットの数
data = [0, 1, 5, 7, 9, 10, 14]


def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance


def std_dev(values):
    return sqrt(variance(values))


print(std_dev(data))
