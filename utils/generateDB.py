import os
import sqlite3
import pandas as pd
from pathlib import Path

class generateDB:
    def __init__(self, df_dict:pd.DataFrame):
        """
        Costructor
        """
        self.df_dict = df_dict


    def createDB(self, df_dict:pd.DataFrame):
        """
        Returns a SQLite3 DB.
        Takes all spreadsheets in data folder and creates a table with each one
        """
        db_dir=Path('./database/anh_data.db')
        # Creates a database
        if os.path.isdir(Path("./database/")):
            print("Initializing database")
            conn = sqlite3.connect(db_dir)
            c = conn.cursor()

            data_types = {'departamento':"text",'municipio':"text",
                            'operadora':"text",'contrato':"text",'campo':"text",
                            "cuenca":"text",'enero':"real",'febrero':"real",'marzo':"real",
                            'abril':"real",'mayo':"real",'junio':"real",'julio':"real",'agosto':"real",
                            'septiembre':"real",'octubre':"real", 'noviembre':"real", 'diciembre':"real"}

            print("Creating tables")
            for year in list(df_dict.keys()):
                i = 0
                query = f"CREATE TABLE IF NOT EXISTS crude_{year} ("
                for col in list(df_dict[year].columns):
                    if col in data_types.keys():
                        data_type = data_types[col]
                        if i == len(list(df_dict[year].columns))-1:
                            constraint = f"{col} {data_type})"
                        else:
                            constraint = f" {col} {data_type}, "
                        i+=1
                    query = query + constraint

                c.execute(f'''{query}''')
                # Write the data to a sqlite table
                df_dict[year].to_sql(f"crude_{year}",  conn, if_exists='replace', index = False)
            print("Dumped tables into database finished")
        else:
            os.mkdir(Path("./database/"))
            db_dir.touch()
            self.createDB(df_dict)
