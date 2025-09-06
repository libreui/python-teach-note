import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///../db/btq.db')
df = pd.read_csv('../db/beijing_tianqi.csv')
df.to_sql('beijing_tq', engine)
print('转换完成')
