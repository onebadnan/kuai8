from utils.openationExcel import get_request_data
from utils.operationJson import OperationJson
from utils.openationExcel import OpenationExcel
from utils.public import *
import json

operationExcel=OpenationExcel()
operationJson=OperationJson()
def setSo():
    '''对不同对视频重新复制'''
    dict1=operationJson.getRequestsData(1)
    print(dict1)

def writeuser(content ):
    '''把用户信息写入到文件中'''
    with open(data_dir(filename='UserInfo'),'w') as f:
        f.write(content)

def getuserInfo( ):
    '''把用户信息写入到文件中'''
    with open(data_dir(filename='UserInfo'),'r') as f:
        return json.loads(f.read())

def getUrl(phoneNum):
    Loginurl=operationExcel.get_url(1)
    userLogin='http://dev.api.kuai8.mobi/1/user/bindphone.json?captcha=6868&phone={0}'.format(phoneNum)
    return userLogin
