# 例3-15 Pythonで中心極限定理を確認する例

# 一様な分布の標本は、平均を取ると正規分布に近づいていく
import random
import plotly.express as px

sample_size = 31
sample_count = 1000

# 中心極限定理： 0.0から1.0の範囲のランダムな値を31個ずつ持つ標本を1000回生成
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / \
    sample_size)
            for _ in range(sample_count)]

y_values = [1 for _ in range(sample_count)]

px.histogram(x=x_values, y = y_values, nbins=20).show()
