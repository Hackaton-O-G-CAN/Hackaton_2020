import numpy as np
import pandas as pd
from glob import glob
from pathlib import Path

class dataProc:
    def __init__(self):
        pass
    def lss(self, expr = './data/*.*'):
        return glob(expr)

    def bringLastMonth(self, filenames:list) -> list:
        self.filenames = filenames
        filenames_str = []

        month_dict = {"ene":1, "feb":2, "mar":3, "abr":4, "may":5,
                    "jun":6, "jul":7, "ago":8, "sep":9, "oct":10,
                    "nov":11, "dic":12}
        i = 0
        for file in filenames:
            file = file.replace("data/","").replace(".xlsx","").replace("data\\","").replace("./","")
            if "2020" not in file:
                filenames_str.append(f"{file}.xlsx")
            else:
                month = file[-3:]
                if month_dict[month] > i:
                    i = month_dict[month]
                    last_month = month
        filenames_str.append(f"2020{last_month}.xlsx")
        filenames_clean = [Path(dir_str) for dir_str in filenames_str]

        return filenames_clean

    def loadData(self) -> pd.DataFrame:
        """
        Returns a dictionary containing a dataframe as value and its corresponding year as a key
        """
        # An empty dictionary is initialized in order to store dataframes by year as key
        df_dict={}

        # Load of files in data directory
        list_files = self.lss()
        print("list files")
        print(list_files)
        years_files = self.bringLastMonth(list_files)
        print("years files")
        print(years_files)

        print("Loading data")
        # For 2020 remove the month in the name

        for year in range(len(years_files)):
            file_dir = years_files[year]
            filename = str(file_dir).replace("data/","").replace(".xlsx","").replace("data\\","")
            file_dir = Path(f"./data/{file_dir}")

            if "2020" in filename:
                df_dict['2020']= pd.read_excel(file_dir)
            else:
                df_dict[filename]= pd.read_excel(file_dir)

        print("Loading data finished")
        return df_dict

    def cleanData(self, df_dict:dict) -> pd.DataFrame:
        """
        Returns a dictionary with years as keys and transformed DataFrames as values
        Clean a dictionary containing keys as yeas and its corresponding Pandas DataFrame
        """
        self.df_dict = df_dict
        print("Cleanning data")
        # Store dataframes in dictionary
        for i in df_dict.keys():
            df_dict[i]=df_dict[i].dropna(axis=0, thresh=2) #delete rows with just nan values
            df_dict[i]=df_dict[i].reset_index(drop=True) #add dpto back as a col
            df_dict[i].columns=df_dict[i].iloc[0].str.lower() #set new first row as cols names
            df_dict[i]=df_dict[i].drop(df_dict[i].index[0]) #drop row in the df with cols names
            #df_dict[i]= df_dict[i].drop(df_dict[i][df_dict[i]["campo"].isnull() & df_dict[i]["operadora"].isnull() & df_dict[i]["municipio"].isnull()].index)#Eliminate the rows where the value of 
            #the field, operator and municipality is null because it  would not be possible to determine these data with the 
            #remaining information.
        print("Cleaning data finsihed")
        return df_dict