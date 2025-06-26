# 例C-7 NOTEASを簡易的に自前で実装した例
import numpy as np
import pandas as pd

temperature = [5, 6, 10, 15,
               20, 24, 28, 30,
               25, 18, 12, 7]
ice_cream_sales = [189, 191, 203, 349,
                   468, 508, 617, 653,
                   550, 404, 302, 226]
crime_rate = [901, 1031, 1111, 1272,
              1343, 1526, 1714, 1646,
              1451, 1252, 1173, 1129]

df = pd.DataFrame({
    "Temperature": temperature,
    "IceCreamSales": ice_cream_sales,
    "CrimeRate": crime_rate
})

from scipy.linalg import expm
from scipy.optimize import minimize


def _h(W):
    """非巡回制約を実装したもの"""
    d = W.shape[0]
    return np.trace(expm(W * W)) - d


def _loss(W, X, l1):
    """回帰損失とL1正則化を実装したもの"""
    n = X.shape[0]
    R = X @ W
    mse = 0.5 / n * np.square(X - R).sum()
    l1 = l1 * np.abs(W).sum()
    return mse + l1


def _grad(W, X, l1):
    """損失の勾配を実装したもの"""
    n = X.shape[0]
    R = X @ W
    grad_m = X.T @ (R - X) / n
    grad_l1 = l1 * np.sign(W)
    return grad_m + grad_l1


def notears(X):
    """
    NOTEARSアルゴリズムを簡易的に実装したもの
    """
    X = X.astype(float)
    n, d = X.shape
    W = np.zeros((d, d), dtype=float)

    alpha = 0.0  # ラグランジュ乗数
    rho = 1.0  # ペナルティ係数
    l1 = 0.01  # L1正則化係数
    _threshold = 10.0  # しきい値
    # 100回反復する
    for it in range(100):
        def obj(w_vec):
            Wmat = w_vec.reshape(d, d)
            loss = _loss(Wmat, X, l1)
            h_val = _h(Wmat)
            aug_lag = loss + alpha * h_val + 0.5 * rho * h_val ** 2
            return aug_lag

        def obj_grad(w_vec):
            Wmat = w_vec.reshape(d, d)
            loss_grad = _grad(Wmat, X, l1)
            h_val = _h(Wmat)
            # 微分する
            E = expm(Wmat * Wmat).T * 2 * Wmat
            aug_grad = loss_grad + (alpha + rho * h_val) * E
            return aug_grad.ravel()

        # SciPyのL-BFGS-Bを使用して最適化を実行する
        sol = minimize(
            obj,
            W.ravel(),
            method="L-BFGS-B",
            jac=obj_grad
        )
        W = sol.x.reshape(d, d)
        h_val = _h(W)
        print(f"Iter {it:02d}: h={h_val:.3e}, rho={rho:.1e}")

        # 収束したか判定する
        if h_val <= 1e-8 or 1e+16 < rho:
            break

        # 乗数を更新する
        alpha += rho * h_val
        # 係数を更新する
        rho *= 10

    # しきい値以下の値のセルを切り落とす
    W[np.abs(W) < _threshold] = 0.0
    return W


causal_matrix = notears(df.values)
print(causal_matrix)

import networkx as nx

# 因果関係の行列をNetworkXの有向グラフに変換する
graph = nx.DiGraph()
cols = df.columns.tolist()

# 因果行列に基づいてエッジを追加する
for i in range(causal_matrix.shape[0]):
    for j in range(causal_matrix.shape[1]):
        if 10 <= abs(causal_matrix[i, j]):  # ゼロでない値のエッジを採用する
            graph.add_edge(cols[i], cols[j])
import matplotlib.pyplot as plt

# 描画する
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)
nx.draw(graph, pos,
        with_labels=True,
        node_size=3000,
        node_color="lightblue", font_size=12, arrowsize=12, arrows=True)
plt.show()
