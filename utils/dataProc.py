import numpy as np
import pandas as pd
from glob import glob
from pathlib import Path


class dataProc:
    def __init__(self):
        pass

    def lss(self, expr='./data/*.*'):
        """
        Gets all files of directory, overrides diferences on directories according to OS.
        """
        return glob(expr)

    def bringLastMonth(self, filenames: list) -> list:
        """
        Bring the last month spreadsheet of the 2020
        """
        self.filenames = filenames
        filenames_str = []

        month_dict = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5,
                      "jun": 6, "jul": 7, "ago": 8, "sep": 9, "oct": 10,
                      "nov": 11, "dic": 12}
        i = 0
        for file in filenames:
            file = file.replace("data/", "").replace(".xlsx",
                                                     "").replace("data\\", "").replace("./", "").replace(".xls","")
            if "2016" in file:
                filenames_str.append(f"{file}.xls")
            elif "2020" not in file:
                filenames_str.append(f"{file}.xlsx")
            else:
                month = file[-3:]
                if month_dict[month] > i:
                    i = month_dict[month]
                    last_month = month
        filenames_str.append(f"2020{last_month}.xlsx")
        filenames_clean = [Path(dir_str) for dir_str in filenames_str]

        return filenames_clean

    def loadData(self) -> dict:
        """
        Returns a dictionary containing a dataframe as value and its corresponding year as a key
        """
        # An empty dictionary is initialized in order to store dataframes by year as key
        df_dict = {}

        # Load of files in data directory
        list_files = self.lss('./data/*.*')
        years_files = self.bringLastMonth(list_files)

        print("Loading data")
        # For 2020 remove the month in the name

        for year in range(len(years_files)):
            file_dir = years_files[year]
            filename = str(file_dir).replace(
                "data/", "").replace(".xlsx", "").replace("data\\", "").replace(".xls","").replace("./","")
            file_dir = Path(f"./data/{file_dir}")

            if "2020" in filename:
                df_dict['2020'] = pd.read_excel(file_dir)
            elif "2016" in filename:
                df_dict['2016'] = pd.read_excel(Path("./data/2016.xls"))
            else:
                df_dict[filename] = pd.read_excel(file_dir)

        print("Loading data finished")
        return df_dict

    def cleanData(self, df_dict: dict) -> dict:
        """
        Returns a dictionary with years as keys and transformed DataFrames as values
        Clean a dictionary containing keys as yeas and its corresponding Pandas DataFrame
        """
        self.df_dict = df_dict
        print("Cleanning data")
        col_order = ['diciembre','noviembre','octubre','septiembre','agosto','julio','junio',
             'mayo','abril','marzo','febrero','enero','campo','contrato','operadora','municipio','departamento']

        # Special considerations taken on problematic datasets
        years_special = ["2015","2017"]

        for year in years_special:
            if year in df_dict.keys():
                df_dict[year] = df_dict[year].dropna(axis=1, thresh=5)

        # Batch of cleanning data for all datasets.
        for i in df_dict.keys():

            # Delete rows with just nan values
            df_dict[i] = df_dict[i].dropna(axis=0, thresh=2)
            df_dict[i] = df_dict[i].dropna(axis=1, thresh=5) #delete columns with just nan values
            
            df_dict[i] = df_dict[i].reset_index(drop=True)

            # Set new first row as cols names
            df_dict[i].columns = df_dict[i].iloc[0].str.lower()

            # drop row in the df with cols names
            df_dict[i] = df_dict[i].drop(df_dict[i].index[0])
            if ("empresa" in df_dict[i]):
                df_dict[i].rename(columns={"empresa": "operadora"}, inplace=True)

            # Special Considerations on cleanning the data
            if ("campo" and "operadora" and "departamento") in df_dict[i].keys():
                df_dict[i] = df_dict[i].drop(df_dict[i][df_dict[i]["campo"].isnull() & df_dict[i]["operadora"].isnull() & df_dict[i]["departamento"].isnull()].index)

            to_lower_case = ["campo", "contrato", "operadora","departamento"]
            for to_lower in to_lower_case:
                if to_lower in df_dict[i].columns:
                    df_dict[i][to_lower] = df_dict[i][to_lower].str.lower()

            # Clean trailling spaces in column names
            for j in list(df_dict[i].columns):
                df_dict[i] = df_dict[i].rename(columns={str(j): str(j.strip())})

            # Puts the columns in a common order for each dataframe
            for j in col_order:
                if j in list(df_dict[i].columns):
                    first_col = df_dict[i].pop(j)
                    df_dict[i].insert(0, j, first_col)

        print("Cleaning data finsihed")
        return df_dict

    def loadBlindData(self) -> dict:
        """
        Returns a dictionary containing a dataframe as value and its corresponding year as a key
        """
        df_dict_blind = {}

        # Load of files in data directory
        list_files_blind = self.lss('./data_blind/*.*')

        for year in range(len(list_files_blind)):
            file_dir = list_files_blind[year]
            filename = str(file_dir).replace("data_blind/", "").replace(".xlsx", "").replace("data\\", "").replace("./","")
            file_dir = Path(f"{file_dir}")

            if "2017" in filename:
                df_dict_blind['2017'] = pd.read_excel(file_dir)
            elif "2018" in filename:
                df_dict_blind["2018"] = pd.read_excel(file_dir)
            elif "2019" in filename:
                df_dict_blind['2019'] = pd.read_excel(file_dir)

        print("Loading data blind test finished")
        return df_dict_blind

    def cleanBlindData(self, df_dict: dict) -> dict:
        """
        Returns a dictionary with years as keys and transformed DataFrames as values
        Clean a dictionary containing keys as yeas and its corresponding Pandas DataFrame
        """
        self.df_dict = df_dict
        print("Cleanning blind data")
        col_order = ['diciembre','noviembre','octubre','septiembre','agosto','julio','junio',
                'mayo','abril','marzo','febrero','enero','campo','contrato','operadora','municipio','departamento']

        # Batch of cleanning data for all datasets.
        for i in df_dict.keys():

            # Delete rows with just nan values
            df_dict[i] = df_dict[i].dropna(axis=0, thresh=2)
            df_dict[i] = df_dict[i].dropna(axis=1, thresh=5) #delete columns with just nan values
            df_dict[i] = df_dict[i].reset_index(drop=True)

            # Set new first row as cols names
            df_dict[i].columns = df_dict[i].columns.str.lower()

            # drop row in the df with cols names
            if ("empresa" in df_dict[i].columns):
                df_dict[i].rename(columns={"empresa": "operadora"}, inplace=True)

            # Special Considerations on cleanning the data
            if ("campo" and "operadora" and "departamento") in df_dict[i].keys():
                df_dict[i] = df_dict[i].drop(df_dict[i][df_dict[i]["campo"].isnull() & df_dict[i]["operadora"].isnull() & df_dict[i]["departamento"].isnull()].index)

            to_lower_case = ["campo", "contrato", "operadora","departamento"]
            for to_lower in to_lower_case:
                if to_lower in df_dict[i].columns:
                    df_dict[i][to_lower] = df_dict[i][to_lower].str.lower()
                    df_dict[i][to_lower] = df_dict[i][to_lower].str.replace(" ","-")

            # Clean trailling spaces in column names
            for j in list(df_dict[i].columns):
                df_dict[i] = df_dict[i].rename(columns={str(j): str(j.strip())})

            # Puts the columns in a common order for each dataframe
            for j in col_order:
                if j in list(df_dict[i].columns):
                    first_col = df_dict[i].pop(j)
                    df_dict[i].insert(0, j, first_col)

        print("Cleaning blind data finsihed")
        return df_dict