# 例4-20 NumPyで行列分解を実行する例

from numpy import array
from numpy.linalg import eig

A = array([
    [1, 2],
    [4, 5]
])

eigenvals, eigenvecs = eig(A)

print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)
