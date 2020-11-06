import os
import pandas as pd
from pathlib import Path
import sqlite3

class generateDB:
    def __init__(self, df_dict:pd.DataFrame):
        self.df_dict = df_dict


    def createDB(self, df_dict:pd.DataFrame):
        db_dir=Path('./database/anh_data.db')
        # Creates a database
        if os.path.isdir(Path("./database/")):
            conn = sqlite3.connect(db_dir)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS users (user_id int, username text)''')
            users = pd.read_csv('./database/user.csv')
            # write the data to a sqlite table
            users.to_sql('users', conn, if_exists='append', index = False)
            print(c.execute('''SELECT * FROM users''').fetchall())
        else:
            os.mkdir(Path("./database/"))
            db_dir.touch()
            self.createDB(df_dict)
