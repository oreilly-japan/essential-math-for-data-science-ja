# 例7-2 SymPyでロジスティック関数をプロットする例

from sympy import *

# ロジスティック（シグモイド）関数
x = symbols('x')
logistic = 1 / (1 + exp(-x))
plot(logistic)
