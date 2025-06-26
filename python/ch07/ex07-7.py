# 例7-7 コスト関数の𝐴2に関する微分を求める例

from sympy import *

A2, y = symbols('A2 Y')
C = (A2 - y)**2
dC_dA2 = diff(C, A2)
print(dC_dA2)