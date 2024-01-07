import pandas as pd
import pyodbc
from sqlalchemy import create_engine

pyodbc.pooling = False
engine = create_engine(
    fr'mssql+pyodbc://sa:cj126414.@192.168.1.7/AnJiServer?driver=ODBC+Driver+17+for+SQL+Server',
    fast_executemany=True)


# class User():
#     metadata = MetaData()
#     Item_version = Table('Item_version', metadata,
#                          Column('Item', String, primary_key=True),
#                          # Add other columns as needed
#                          Column('C_version', String),
#                          Column('H_version', String))
#
#     # Create the table if it doesn't exist
#     metadata.create_all(engine)


def Query(sql):
    try:
        df = pd.read_sql_query(sql, engine)
        return df
    except Exception as e:
        print(e)
        # 返回空的DataFrame
        return pd.DataFrame()
