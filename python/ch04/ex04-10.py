# 例4-10 複雑な変換の例

from numpy import array

# iハットとjハットを宣言する
i_hat = array([2, 3])
j_hat = array([2, -1])

# iハットとjハットを使って基底ベクトルの行列を作成する
# 行を列に転置する必要がある
basis = array([i_hat, j_hat]).transpose()

# ベクトルvを宣言する
v = array([2,1])

# 内積によりvを変換して新たなベクトルを作り出す
new_v = basis.dot(v)

print(new_v)
