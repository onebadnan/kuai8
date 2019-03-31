class ExcelVariable:
    caseId = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5


def getCaseID():
    return ExcelVariable.caseId


def get_url():
    return ExcelVariable.url


def get_request_data():
    return ExcelVariable.request_data


def get_expect():
    return ExcelVariable.expect


def get_result():
    return ExcelVariable.result


def get_headerValue():
    '''获取请求他'''
    headers = {
        'Host': 'dev.api.kuai8.mobi',
        'cp-uuid': '4c51cc98f0bfca72d8a38e09c8c7b32bc9081902',
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid': '3-100',
        'cp-appid': '800',
        'cp-sign': '3657f82f2c814ff420d6ecfaafa8dab8',
        'cp-ver': '1.1.3',
        'cp-time': '1553224952',
        'cp-token': 'y-B5LR6q-WnVMfZlsZLktSGT6Qb-Eiu~seh~VMI7BD0_',  # 快友197
        'cp - os': 'ios',
        'cp - vend': 'kuai8',
        'cp - oem': 'iphone8',
        'Accept - Language': 'zh-Hans-CN;q=1',
        'cp - sver': '12.1.4',
        'Accept': '* / *',
        'cp - channel': 'appstore',
        'Accept - Encoding': 'gzip, deflate',
        'BodyEncode': '1',
        'AppKey': 'kuai8-ios',
        'Connection': 'keep-alive'}
    return headers

def get_headerInfo():
    '''获取请求他'''
    headers = {
        'Host': 'dev.api.kuai8.mobi',
        'cp-uuid': '4c51cc98f0bfca72d8a38e09c8c7b32bc9081902',
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid': '3-100',
        'cp-appid': '800',
        'cp-sign': '3657f82f2c814ff420d6ecfaafa8dab8',
        'cp-ver': '1.1.3',
        'cp-time': '1553224952',
        'cp-token': 'y-B5LR6q-WnVMfZlsZLktSGT6Qb-Eiu~seh~VMI7BD0_',  # 快友197
        'cp - os': 'ios',
        'cp - vend': 'kuai8',
        'cp - oem': 'iphone8',
        'Accept - Language': 'zh-Hans-CN;q=1',
        'cp - sver': '12.1.4',
        'Accept': '* / *',
        'cp - channel': 'appstore',
        'Accept - Encoding': 'gzip, deflate',
        'BodyEncode': '1',
        'AppKey': 'kuai8-ios',
        'Content - Type':'application /x-www-form-urlencoded',
        'Connection': 'keep-alive'}
    return headers