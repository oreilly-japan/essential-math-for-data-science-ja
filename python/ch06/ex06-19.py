# 例6-19 scikit-learnのstratifyオプションを使ってクラス分布を維持する例

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

# データを読み込む
df = pd.read_csv("https://tinyurl.com/y6r7qjrp", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test =  \
    train_test_split(X, Y, test_size=0.33, stratify=Y)

model = LogisticRegression(penalty=None)
model.fit(X_train, Y_train)

Y_pred_prob = model.predict_proba(X_test)[:, 1]

# AUCを使ってスコアリングする
auc_score = roc_auc_score(Y_test, Y_pred_prob)
print("AUC: %.3f" % auc_score)
