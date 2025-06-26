# 例4-5 PythonでNumPyを使って2つのベクトルを加算する例

from numpy import array

v = array([3,2])
w = array([2,-1])

# ベクトルを足し合わせる
v_plus_w = v + w

# 加算したベクトルを出力する
print(v_plus_w)
