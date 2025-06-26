# 例C-1 データセットを月ごとに並べてプロットする例

import matplotlib.pyplot as plt
import japanize_matplotlib

import numpy as np
import pandas as pd

# アイスクリームの売上（万円）
ice_cream_sales = [189, 191, 203, 349,
                   468, 508, 617, 653,
                   550, 404, 302, 226]
# 犯罪件数（件）
crime_rate = [901, 1031, 1111, 1272,
              1343, 1526, 1714, 1646,
              1451, 1252, 1173, 1129]
# データフレームを作成
df = pd.DataFrame({
    "IceCreamSales": ice_cream_sales,
    "CrimeRate": crime_rate
})

# x軸を月としてグラフを重ねて描画
fig, ax1 = plt.subplots(figsize=(10, 6))

# IceCreamSalesを左側y軸で描画
color = 'tab:blue'
ax1.set_xlabel('月', fontsize=16)
ax1.set_ylabel('アイスクリームの売上 (万円)', color=color, fontsize=16)
ax1.plot(df.index + 1, df['IceCreamSales'], marker='o', color=color, label='アイスクリームの売上')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(df.index + 1)
#
# # CrimeRateを右側y軸で描画
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('犯罪件数 (件)', color=color, fontsize=16)
ax2.plot(df.index + 1, df['CrimeRate'], marker='s', linestyle='--', color=color, label='犯罪件数')
ax2.tick_params(axis='y', labelcolor=color)
# 凡例を追加
ax1.legend(loc='upper left', fontsize=16)  # 左側y軸の凡例
ax2.legend(loc='upper right', fontsize=16)  # 右側y軸の凡例
#
# # タイトルとグリッド設定
fig.suptitle('ある地域のアイスクリームの売上と犯罪件数の推移（月ごと）', fontsize=20)
fig.tight_layout()
fig.subplots_adjust(top=0.9)
ax1.grid(True)

plt.show()
# --- 分析 ---

from scipy.stats import pearsonr

# 相関行列を確認
correlation_matrix = df.corr()
print(correlation_matrix)

# 相関係数とp値を計算
correlation, p_value = pearsonr(df['CrimeRate'], df['IceCreamSales'])

# 結果を表示
print(f"相関係数: {correlation:.06f}")
print(f"p値: {p_value:.10f}")



