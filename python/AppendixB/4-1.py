# 演習4-1

from numpy import array

v = array([1,2])

i_hat = array([2, 0])
j_hat = array([0, 1.5])

# 直線を当てはめる
basis = array([i_hat, j_hat])

# 内積によりベクトルvをwに変換する
w = basis.dot(v)

print(w)
