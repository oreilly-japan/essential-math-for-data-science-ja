# A-3 ゼロから二項分布を実装する例

# 階乗：ある整数から1までの連続する整数を順番に掛け合わせたもの
# 例: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

# 二項分布に必要な係数を生成する
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))

# 試行回数nのうち成功確率pでk回成功する確率を二項分布で求める
def binomial_distribution(k: int, n: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * (1.0 - p) ** (n - k)

# 成功確率が90%の試行を10回行う
n = 10
p = 0.9

for k in range(n + 1):
    probability = binomial_distribution(k, n, p)
    print("{0} - {1}".format(k, probability))
