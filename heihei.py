import requests
def get_headers(abid='1-100'):
    headers = {
        'Host': 'dev.api.kuai8.mobi',
        'cp-uuid': '4c51cc98f0bfca72d8a38e09c8c7b32bc9081902',
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid': abid,
        'cp-appid': '800',
        'cp-sign': '3657f82f2c814ff420d6ecfaafa8dab8',
        'cp-ver': '1.1.3',
        'cp-time': '1553224952',
        'cp-token': '-GzKz1I3fE-s4QGJzbXPmLlSAQCj8uUvra9KWQYh23I_',
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
headers=get_headers()
url = 'http://dev.api.kuai8.mobi/1/feed/list.json?count=15&page=2'
r = requests.get(url, headers=headers)
print(r.json())
