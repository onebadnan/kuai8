import requests
import json
def swipe():
    headers = {
        'Host': 'api.kuai8.mobi',
        'cp-uuid': '4c51cc98f0bfca72d8a38e09c8c7b32bc9081902',
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid':'3-100',
        'cp-appid':'800',
        'cp-sign': '3657f82f2c814ff420d6ecfaafa8dab8',
        'cp-ver': '1.1.3',
        'cp-time':'1553224952',
        'cp-token':'y-B5LR6q-WnVMfZlsZLktSGT6Qb-Eiu~seh~VMI7BD0_',#快友197
        'cp - os': 'ios',
        'cp - vend': 'kuai8',
        'cp - oem': 'iphone8',
        'Accept - Language': 'zh-Hans-CN;q=1',
        'cp - sver':'12.1.4',
        'Accept':'* / *',
        'cp - channel':'appstore',
        'Accept - Encoding':'gzip, deflate',
        'BodyEncode':'1',
        'AppKey':'kuai8-ios',
        'Connection':'keep-alive'}
    '''
    横滑 url=http://dev.api.kuai8.mobi/1/feed/topic.json?smids=&stid=spS08t-F8B4
    竖滑 url=http://dev.api.kuai8.mobi/1/feed/list.json?count=15&page=2
    '''
    url='http://api.kuai8.mobi/1/feed/topic.json?smids=&stid=spS08t-F8B4"' #竖滑
    r=requests.get(url,headers=headers)
    print(json.dumps(r.json(),indent=True,ensure_ascii=False))

for i in range(1,10):
    swipe()
