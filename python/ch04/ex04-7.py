# 例4-7 NumPyによる行列とベクトルの積

from numpy import array

# iハットとjハットの基底ベクトルの行列を生成する
basis = array(
    [[3, 0],
     [0, 2]]
 )

# ベクトルvを宣言する
v = array([1,1])

# 内積によりvを変換して新たなベクトルを作り出す
new_v = basis.dot(v)

print(new_v)
