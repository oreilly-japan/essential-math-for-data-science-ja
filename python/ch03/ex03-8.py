# 例3-8 標本の標準偏差を求める例

from math import sqrt

# 飼っているペットの数
data = [0, 1, 5, 7, 9, 10, 14]


def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / \
      (len(values) - (1 if is_sample else 0))

    return _variance


def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))


print("VARIANCE = {}".format(variance(data, is_sample=True)))
print("STD DEV = {}".format(std_dev(data, is_sample=True)))
