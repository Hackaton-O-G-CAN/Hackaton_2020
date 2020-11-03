import pandas as pd
import numpy as np
from glob import glob
import os
class cleanData:
    def __init__(self):
        pass
    def lss(self, expr = f'.{os.path.sep}data{os.path.sep}*.*'):
        return glob(expr)

    def bringLastMonth(self, filenames:list) -> list:
        self.filenames = filenames
        filenames_clean = []

        month_dict = {"ene":1, "feb":2, "mar":3, "abr":4, "may":5,
                    "jun":6, "jul":7, "ago":8, "sep":9, "oct":10,
                    "nov":11, "dic":12}
        i = 0
        for file in filenames:
            file = file.replace(f".{os.path.sep}data{os.path.sep}","").replace(".xlsx","")
            if "2020" not in file:
                filenames_clean.append(file)
            else:
                month = file[-3:]
                if month_dict[month] > i:
                    i = month_dict[month]
                    last_month = month
        filenames_clean.append(f"2020{last_month}")
        return filenames_clean

    def cleanData(self) -> pd.DataFrame:
        # An empty dictionary is initialized in order to store dataframes by year as key
        df_dict={}

        # Load of files in data directory
        list_files = self.lss()
        years_files = self.bringLastMonth(list_files)

        # For 2020 remove the month in the name
        for year in years_files:
            file_dir = f".{os.path.sep}data{os.path.sep}{year}.xlsx"
            #file_dir = f"{year}.xlsx"
            if "2020" in year:
                df_dict['2020']= pd.read_excel(file_dir)
            else:
                df_dict[year]= pd.read_excel(file_dir)

        # Store dataframes in dictionary
        for i in df_dict.keys():
            df_dict[i]=df_dict[i].dropna(axis=0, thresh=2) #delete rows with just nan values
            df_dict[i]=df_dict[i].reset_index(drop=True) #add dpto back as a col
            df_dict[i].columns=df_dict[i].iloc[0].str.lower() #set new first row as cols names
            df_dict[i]=df_dict[i].drop(df_dict[i].index[0]) #drop row in the df with cols names
            if ("empresa" in df_dict[i]): df_dict[i].rename(columns={"empresa": "operadora"}, inplace=True)
            df_dict[i]= df_dict[i].drop(df_dict[i][df_dict[i]["campo"].isnull() & df_dict[i]["operadora"].isnull() & df_dict[i]["departamento"].isnull() ].index)#Eliminate the rows where the value of 
            #the field, operator and municipality is null because it  would not be possible to determine these data with the 
            #remaining information.

        return df_dict
