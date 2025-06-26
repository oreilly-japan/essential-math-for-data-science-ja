# 例8-2 PythonでSQLAlchemyを使ってSQLクエリーを実行する例
# 事前にSQLiteデータベースのファイルをダウンロードする必要があります。
#
# 例）
# wget -O thunderbird_manufacturing.db https://bit.ly/3F8heTS

from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///thunderbird_manufacturing.db')
conn = engine.connect()

stmt = text("SELECT * FROM CUSTOMER")
results = conn.execute(stmt)
for customer in results:
    print(customer)
