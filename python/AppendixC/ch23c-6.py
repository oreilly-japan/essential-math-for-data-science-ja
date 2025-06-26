# 例C-6 因果行列から因果グラフをプロットする例
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
data = df.values.astype(float)
cols = df.columns.tolist()

from castle.algorithms import Notears

# NOTEARSアルゴリズムによって因果行列（因果関係の行列）を求める
notears = Notears()
notears.learn(data=df.values, columns=df.columns)
print(notears.causal_matrix)

import networkx as nx

# 因果行列をNetworkXの有向グラフに変換する
causal_matrix = notears.causal_matrix
graph = nx.DiGraph()

# 因果行列に基づいてエッジを追加する
for i in range(causal_matrix.shape[0]):
    for j in range(causal_matrix.shape[1]):
        if causal_matrix[i, j] != 0:  # ゼロでない値のエッジを採用する
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
