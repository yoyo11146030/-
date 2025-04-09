from database import engine
from models import Base

# 寫入所有 models 到資料庫
Base.metadata.create_all(bind=engine)

print("✅ 資料表已成功建立！")