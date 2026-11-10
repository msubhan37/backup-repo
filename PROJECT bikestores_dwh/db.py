import pyodbc
import pandas as pd
from sqlalchemy import create_engine

SERVER_NAME = "localhost"
DATABASE_NAME = "BikeStores"
DRIVER = "ODBC Driver 17 for SQL Server"

connection_string = (

    f"mssql+pyodbc://@{SERVER_NAME}/{DATABASE_NAME}"
    f"?driver={DRIVER.replace(' ', '+')}&Trusted_Connection=yes"

)

engine = create_engine(connection_string)

try:
    with engine.connect() as conn:
        print("DataBase Connected successfully!")
except Exception as e:
    print("Connection Failed:", e)


query = "SELECT * FROM sales.customers"

df = pd.read_sql(query, engine)

print(df)