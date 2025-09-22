import os
from dotenv import load_dotenv
import pandas as pd
import psycopg
import pandas as pd

# Load environment variables
load_dotenv()

class MyDenodoDB:
    def __init__(self):
        """
        This function sets initial attributes
        """
        self.user = os.getenv("DENODO_USER")
        self.password = os.getenv("DENODO_PASSWORD")
        self.host = os.getenv("DENODO_HOST")
        self.port = os.getenv("DENODO_PORT")
        self.dbname = os.getenv("DENODO_DBNAME")
        # print(f"host {self.host}, port {self.port}, dbname {self.dbname}, user {self.user}")
        self.connection = None
    
    def connect(self):
        """
        This function opens a connection to your Postgresql database
        """
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

    def query_to_df(self, sql: str, params=None) -> pd.DataFrame:
        """
        This function helps to retrieve data from a PostgreSQL database
        Args:
            sql (str): this is a sql statement e.g. select column1 from table
            params (_type_, optional): This parameter is optional. Only if you want to work with parameters. Defaults to None.

        Returns:
            pd.DataFrame: _description_
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params or {})
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                return pd.DataFrame(rows, columns = columns)
        except psycopg.DatabaseError as error:
            # error, = e.args
            print(f"❌ SQL execution failed: {error}")
            return pd.DataFrame()

    def close(self):
        """
        This function closes the connection to your Postgresql database
        """
        if self.connection:
            self.connection.close()