import os
from dotenv import load_dotenv
import pandas as pd
import psycopg
import pandas as pd

# Load environment variables
load_dotenv()

class MyDenodoDB:
    def __init__(self):
        self.user = os.getenv("DENODO_USER")
        self.password = os.getenv("DENODO_PASSWORD")
        self.host = os.getenv("DENODO_HOST")
        self.port = os.getenv("DENODO_PORT")
        self.dbname = os.getenv("DENODO_DBNAME")
        # print(f"host {self.host}, port {self.port}, dbname {self.dbname}, user {self.user}")
        self.connection = None
    
    def connect(self):
        try:
            self.connection = psycopg.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
        
        except psycopg.OperationalError as oe:
            print("❌ Operational error: Could not connect to the database.")
            print("Details:", oe)

        except psycopg.DatabaseError as de:
            print("❌ Database error occurred.")
            print("Details:", de)

        except Exception as e:
            print("❌ Unexpected error:", e)

    def close(self):
        if self.connection:
            self.connection.close()
    
    def query_to_df(self, sql, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or {})
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                return pd.DataFrame(rows, columns = columns)
        except psycopg.DatabaseError as e:
            error, = e.args
            print(f"❌ SQL execution failed: {error.message}")
            return pd.DataFrame()
