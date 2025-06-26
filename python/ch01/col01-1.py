# コラム SymPyによる総和

from sympy import *

i,n = symbols('i n')

# 1からnまで順に反復し、各要素iを乗算して合計する
summation = Sum(2*i,(i,1,n))

# nを5に指定し、1から5までの数を反復する
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())
