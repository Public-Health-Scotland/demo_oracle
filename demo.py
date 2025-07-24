import os
from dotenv import load_dotenv
import oracledb
import pandas as pd

# load sensitive data from .env file
load_dotenv()

# start connection
oracledb.init_oracle_client()

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN")
)

query = "SELECT LASTNAME, EMAIL FROM ldap_users"

# Load the result into a DataFrame
cursor = connection.cursor()
cursor.execute(query)
# for row in cursor:
#     print(row)

columns = [col[0] for col in cursor.description]
rows = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(rows, columns=columns)
print(df.head())