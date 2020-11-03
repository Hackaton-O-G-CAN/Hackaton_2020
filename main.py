from utils import downloadData
from utils import cleanData

if __name__ == "__main__":

     def run():

          a = downloadData.downloadData()
          a.getData()
          b = cleanData.cleanData()
          df_dict = b.cleanData()
     run()
