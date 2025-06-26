# 例6-14 ロジスティック回帰の𝑅2を求める例

import pandas as pd
from math import log, exp

patient_data = list(pd.read_csv('https://bit.ly/33ebs2R', delimiter=",") \
                                .itertuples())

# ロジスティック回帰の係数
b0 = -3.17580504
b1 = 0.69268939

def logistic_function(x):
    p = 1.0 / (1.0 + exp(-(b0 + b1 * x)))
    return p

# 適合度の対数尤度を求める
log_likelihood_fit = sum(log(logistic_function(p.x)) * p.y +
                         log(1.0 - logistic_function(p.x)) * (1.0 - p.y)
                         for p in patient_data)

# 対数尤度を求める
likelihood = sum(p.y for p in patient_data) / len(patient_data)

log_likelihood = sum(log(likelihood) * p.y + log(1.0 - likelihood) * (1.0 - p.y) \
    for p in patient_data)

# 決定係数$R^2$を求める
r2 = (log_likelihood - log_likelihood_fit) / log_likelihood
print(r2)