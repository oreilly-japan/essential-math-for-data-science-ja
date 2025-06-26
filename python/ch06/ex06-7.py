# 例6-7 SymPyでロジスティック回帰の結合尤度を求める関数の例

from sympy import *

m = Symbol('m')
b = Symbol('b')
x = Function('x')
y = Function('y')
i = Symbol('i')
n = Symbol('n')

joint_likelihood = Sum(log((1.0 / (1.0 + exp(-(b + m * x(i))))) ** y(i) * \
                           (1.0 - (1.0 / (1.0 + exp(-(b + m * x(i)))))) ** (1 - y(i))), (i, 0, n))
print(joint_likelihood)
