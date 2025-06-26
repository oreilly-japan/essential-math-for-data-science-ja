# A-11 PythonのPuLPを使って線形計画法を求める例

# 対象のグラフ https://www.desmos.com/calculator/iildqi2vt7

from pulp import *

# 変数を定義する
x = LpVariable("x", 0)   # 0<=x
y = LpVariable("y", 0) # 0<=y

# 問題を定義する
prob = LpProblem("factory_problem", LpMaximize)

# 制約を定義する
prob += x + 3*y <= 20
prob += 6*x +2*y <= 45

# 最大化する目的関数を定義する
prob += 200*x + 300*y

# 問題を求める
status = prob.solve()
print(LpStatus[status])

# 結果を出力する
print(value(x))
print(value(y))
