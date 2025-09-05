import os
from dotenv import load_dotenv
import pandas as pd
import psycopg
import pandas as pd

load_dotenv()

host = os.getenv("DENODO_HOST")
port = os.getenv("DENODO_PORT")
dbname = os.getenv("DENODO_DBNAME")
user = os.getenv("DENODO_USER")
password = os.getenv("DENODO_PASSWORD")

print(f"host {host}, port {port}, dbname {dbname}, user {user}, password {password}")

connection = psycopg.connect(
    host = host,
    port = port,
    dbname = dbname,
    user = user,
    password = password
)

cursor = connection.cursor()
cursor.execute("select 1 as colname")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
print(pd.DataFrame(rows, columns = columns))
