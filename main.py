from utils import dataProc
from utils import downloadData
from utils import generateDB

if __name__ == "__main__":

    def run():

        download = downloadData.downloadData()
        download.getData()

        data = dataProc.dataProc()
        df = data.loadData()

        df_dict = data.cleanData(df)

        db = generateDB.generateDB(df_dict)
        db.createDB(df_dict)

    run()
