# 例4-16 行列式が0となる例

from numpy.linalg import det
from numpy import array

i_hat = array([3, -1.5])
j_hat = array([-2, 1])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print(determinant)
