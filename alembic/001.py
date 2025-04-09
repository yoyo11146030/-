from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:Aa221511%%40@localhost/sports_db")
try:
    with engine.connect() as connection:
        print("資料庫連線成功")
except Exception as e:
    print(f"資料庫連線失敗: {e}")