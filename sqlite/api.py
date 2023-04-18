import sqlite3
import pandas as pd

class SQLite_Connect:

    def __init__(self, db_name):
        self.db_name = db_name

        self.connect()

        # Creating a cursor
        self.c = self.conn.cursor()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
    
    def execute_sql(self, q):

        # Create a table
        self.c.execute(q)
        self.conn.commit()

    def df_to_sqlite(self, df, table, replace = 'fail'):
        df.to_sql(table, self.conn, if_exists= replace)
        self.conn.commit()
        
    def query(self, q):

        self.c.execute(q)
        tuplist = self.c.fetchall()
        return pd.DataFrame(tuplist)