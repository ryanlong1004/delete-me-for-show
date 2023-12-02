"""
pip install mysql.connector sqlalchemy pandas
"""

from urllib.parse import quote_plus
import mysql.connector as connection
import pandas as pd
from sqlalchemy import create_engine

class DbMySQL:
    
    def __init__(self):
        self.password = 'xxxxxxx@xxxx' # passwords with at symbols result in 'quote_plus'
        self.engine = create_engine(f"mysql+pymysql://spot_reader:{quote_plus(self.password)}@10.251.3.131:3306/spotnws")
        self.conn = connection.connect(
            host="localhost",  # your host, usually localhost
            user="user",  # your username
            passwd="xxxxxx@xxx",  # your password
            db="",
            use_pure=True,
        )
        
    def _query(self, query):
        for batch in pd.read_sql_query(query, con=self.engine, chunksize=10):
           for item in batch.itertuples(index=False):
               yield item
    