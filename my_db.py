import os
from dotenv import load_dotenv
import oracledb
import pandas as pd

# Load environment variables
load_dotenv()

class MyOracleDB:
    def __init__(self):
        """
        This function sets initial attributes
        """
        self.user = os.getenv("ORACLE_USER")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.dsn = os.getenv("ORACLE_DSN")
        # print(f"Connected to dsn {self.dsn}, user {self.user}")
        self.connection = None

    def connect(self):
        """
        This function opens a connection to your oracle database
        """
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

    def query_to_df(self, sql: str, params=None) -> pd.DataFrame:
        """
        This function helps to retrieve data from an Oracle database
        Args:
            sql (str): this is a sql statement e.g. select column1 from table
            params (_type_, optional): This parameter is optional. Only if you want to work with parameters. Defaults to None.

        Returns:
            pd.DataFrame: It returns a pandas dataframe
        """
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

    def close(self):
        """
        This function closes the connection to your oracle database
        """
        if self.connection:
            self.connection.close()