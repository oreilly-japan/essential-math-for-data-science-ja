# 例3-2 Pythonで加重平均を求める例

# 3回の中間試験に0.20の重みを、卒業試験に0.40の重みを与える。
sample = [90, 80, 63, 87]
weights = [0.20, 0.20, 0.20, 0.40]

weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights)

print(weighted_mean)
