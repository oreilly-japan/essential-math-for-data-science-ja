# 例4-12 変換を逆順に適用する例

from numpy import array

# 変換1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# 変換2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# 最初にせん断を適用し、その後に回転を適用する
combined = transform1 @ transform2

# 試しに表示する
print("COMBINED MATRIX:\n {}".format(combined))

v = array([1, 2])
print(combined.dot(v))