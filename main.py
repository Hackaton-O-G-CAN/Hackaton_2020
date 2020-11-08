from utils import dataProc
from utils import downloadData
from utils import generateWeb
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

        web = generateWeb.generateWeb(df_dict)
        web.parseHTML(df_dict)

        data = dataProc.dataProc()
        df = data.loadBlindData()
        df_blind = data.cleanBlindData(df)
    run()
