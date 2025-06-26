# 例8-3 SQLクエリーをPandasのDataFrameの形式で取り込む例
# 事前にSQLiteデータベースのファイルをダウンロードする必要があります。
#
# 例）
# wget -O thunderbird_manufacturing.db https://bit.ly/3F8heTS

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///thunderbird_manufacturing.db')
conn = engine.connect()

df = pd.read_sql("SELECT * FROM CUSTOMER", conn)
print(df)
