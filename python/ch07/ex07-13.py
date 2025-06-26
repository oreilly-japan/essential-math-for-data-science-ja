# 例7-13 scikit-learnを使ったニューラルネットワークの分類器の例

import pandas as pd
# データを読み込む
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('https://bit.ly/3GsNzGt', delimiter=",")

# 入力変数（すべての行、最終列を除くすべての列）を抽出する
# 加えて、スケーリングも実施する
X = (df.values[:, :-1] / 255.0)

# 出力列（すべての行、最終列）を抽出する
Y = df.values[:, -1]

# 訓練用データセットとテスト用データセットに分割する
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

nn = MLPClassifier(solver='sgd',
                   hidden_layer_sizes=(3, ),
                   activation='relu',
                   max_iter=100_000,
                   learning_rate_init=0.05)

nn.fit(X_train, Y_train)

# 重みと偏りを表示する
print(nn.coefs_ )
print(nn.intercepts_)

print("Training set score: %f" % nn.score(X_train, Y_train))
print("Test set score: %f" % nn.score(X_test, Y_test))
