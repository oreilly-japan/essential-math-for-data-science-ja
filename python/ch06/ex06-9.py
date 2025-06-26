# 例6-9 従業員データを使って多変数ロジスティック回帰を実行する例

import pandas as pd
from sklearn.linear_model import LogisticRegression

employee_data = pd.read_csv("https://tinyurl.com/y6r7qjrp")

# 独立変数のカラムを取得する
inputs = employee_data.iloc[:, :-1]

# 従属変数"did_quit"のカラムを取得する
output = employee_data.iloc[:, -1]

# ロジスティック回帰を構築する
fit = LogisticRegression(penalty=None).fit(inputs, output)

# 係数を出力する
print("COEFFICIENTS: {0}".format(fit.coef_.flatten()))
print("INTERCEPT: {0}".format(fit.intercept_.flatten()))

# 対話型のUIで新しい従業員のデータに対して予測する
def predict_employee_will_stay(sex, age, promotions, years_employed):
    prediction = fit.predict([[sex, age, promotions, years_employed]])
    probabilities = fit.predict_proba([[sex, age, promotions, years_employed]])
    if prediction == [[1]]:
        return "WILL LEAVE: {0}".format(probabilities)
    else:
        return "WILL STAY: {0}".format(probabilities)

# 予測をテストする
while True:
    n = input("Predict employee will stay or leave {sex}, \
        {age},{promotions},{years employed}: ")
    (sex, age, promotions, years_employed) = n.split(",")
    print(predict_employee_will_stay(int(sex), int(age), int(promotions),
          int(years_employed)))
