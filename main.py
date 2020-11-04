from utils import downloadData
from utils import dataProc

if __name__ == "__main__":

     def run():

          download = downloadData.downloadData()
          download.getData()

          data = dataProc.dataProc()
          df = data.loadData()

          df_dict = data.cleanData(df)

          print(df_dict.keys())
     run()
