# 例1-27 Pythonによる積分の近似（並べる長方形を1,000個に変更）

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)

    return total_sum * delta_x


def my_function(x):
    return x ** 2 + 1


area = approximate_integral(a=0, b=1, n=1000, f=my_function)

print(area)
