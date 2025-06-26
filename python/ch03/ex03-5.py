# 例3-5 Pythonで最頻値を求める例

from collections import defaultdict

# 飼っているペットの数
sample = [1, 3, 2, 5, 7, 0, 2, 3]


def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes

print(mode(sample))

