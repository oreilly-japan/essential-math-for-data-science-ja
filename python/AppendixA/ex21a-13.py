# A-13 scikit-learnのニューラルネットワークで手書きの数字の分類器を構築する例

import numpy as np
import pandas as pd
# データを読み込む
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('https://bit.ly/3ilJc2C', compression='zip', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
# ここで線形スケーリングを行う
X = (df.values[:, :-1] / 255.0)

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 各グループの標本数をカウントし、標本が偏りなく均衡が取れていることを確認する
print(df.groupby(["class"]).agg({"class" : [np.size]}))

# 訓練用データとテスト用データを分割する。
# 'stratify'パラメーターを指定し、各クラスのデータが、
# 分割後の両方のデータセットも元の割合を保つようする。
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
    test_size=0.33, random_state=10, stratify=Y)

nn = MLPClassifier(solver='sgd',
                   hidden_layer_sizes=(100, ),
                   activation='logistic',
                   max_iter=480,
                   learning_rate_init=0.1)

nn.fit(X_train, Y_train)

print("Training set score: %f" % nn.score(X_train, Y_train))
print("Test set score: %f" % nn.score(X_test, Y_test))

# ヒートマップを表示する
import matplotlib.pyplot as plt
fig, axes = plt.subplots(4, 4)

# 全体の最小値と最大値を使って、全ての重みを同じ尺度で比較できるようにする
vmin, vmax = nn.coefs_[0].min(), nn.coefs_[0].max()
for coef, ax in zip(nn.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray,
               vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
