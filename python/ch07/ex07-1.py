# 例7-1 ReLU関数をプロットする例

from sympy import *

# ReLUをプロットする
x = symbols('x')
relu = Max(0, x)
plot(relu)
