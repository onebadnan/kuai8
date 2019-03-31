from utils.public import *
import json
from utils.openationExcel import OpenationExcel
class OperationJson:
    def __init__(self):
        self.excel=OpenationExcel()
    def getReadJson(self):
        with open(data_dir(filename='RequestData.json'),encoding='utf-8') as f:
            data=json.load(f)
            return data

    def getRequestsData(self,row):
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])
if __name__ == '__main__':
    opera=OperationJson()
    print(opera.getRequestsData(3))
