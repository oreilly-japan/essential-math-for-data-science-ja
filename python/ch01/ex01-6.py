# 例1-6 Pythonで一次関数を宣言する例

def f(x):
    return 2 * x + 1


x_values = [0, 1, 2, 3]

for x in x_values:
    y = f(x)
    print(y)
