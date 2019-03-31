import requests
from utils.excle_data import *
from utils.openationExcel import OpenationExcel
from utils.operationJson import OperationJson

operationExcle = OpenationExcel()


def checkHeader(row, f1=None, f2=None):
    '''检测请求头'''
    url = operationExcle.get_url(row)
    url = url.split('/')
    if url[5] == 'bindphone.json?captcha=6868&phone=18810037430':
        return f1
    elif url[5] != 'bindphone.json?captcha=6868&phone=18810037430':
        return f2


# print(checkHeader(3))

class method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excle = OpenationExcel()

    def post(self, row):
        try:
            r = requests.post(url=self.excle.get_url(row=row),
                              data=self.operationJson.getRequestsData(row),
                              headers=checkHeader(row=row, f1=get_headerValue(), f2=get_headerInfo()),
                              timeout=6)
            return r
        except Exception as e:
            raise RuntimeError("接口请求发生异常的错误")

    def post2(self, row, data=None):
        try:
            r = requests.post(url=self.excle.get_url(row=row),
                              data=data,
                              headers=checkHeader(row=row, f1=get_headerValue(), f2=get_headerInfo()),
                              timeout=6)
            return r
        except Exception as e:
            raise RuntimeError("接口请求发生异常的错误")

    def get(self, url, params=None):
        try:
            r = requests.get(
                # url=self.excle.get_url(row=row),
                url=url,
                headers=get_headerValue(),
                params=params,
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError("接口请求发生异常的错误")


class IsContent:
    def __init__(self):
        self.excel = OpenationExcel()

    def isContent(self, row, str2):
        flag = None
        if self.excel.get_expect(row) in str2:
            flag = True
        else:
            flag = False
        return flag
