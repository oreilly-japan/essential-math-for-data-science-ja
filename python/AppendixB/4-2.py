# 演習4-2

from numpy import array

v = array([1,2])

i_hat = array([-2, 1])
j_hat = array([1, -2])

# 直線を当てはめる
basis = array([i_hat, j_hat])

# 内積によりベクトルvをwに変換する
w = basis.dot(v)

print(w)
