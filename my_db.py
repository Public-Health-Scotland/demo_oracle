import os
from dotenv import load_dotenv
import oracledb
import pandas as pd

# Load environment variables
load_dotenv()

class MyOracleDB:
    def __init__(self):
        self.user = os.getenv("ORACLE_USER")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.dsn = os.getenv("ORACLE_DSN")
        # print(f"Connected to {self.user} {self.password} {self.dsn}")
        self.connection = None

    def connect(self):
        oracledb.init_oracle_client()
        try:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )    
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"❌ Oracle connection failed: {error.message}")
            raise # Re-raise the exception if you want it to propagate


    def close(self):
        if self.connection:
            self.connection.close()
    
    def query_to_df(self, sql, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or {})
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                return pd.DataFrame(rows, columns=columns)
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"❌ SQL execution failed: {error.message}")
            return pd.DataFrame()  # Return empty DataFrame on failure

