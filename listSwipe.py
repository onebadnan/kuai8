import get_token
import requests
import json
import xlutils
import csv

def get_headers(abid='1-100'):
    token = get_token.get_token()
    headers = {
        'Host': 'dev.api.kuai8.mobi',
        'cp-uuid': '4c51cc98f0bfca72d8a38e09c8c7b32bc9081902',
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid': abid,
        'cp-appid': '800',
        'cp-sign': '3657f82f2c814ff420d6ecfaafa8dab8',
        'cp-ver': '1.1.3',
        'cp-time': '1553224952',
        'cp-token': str(token),
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

postitions = []
def onSwipe():
    url = 'http://dev.api.kuai8.mobi/1/feed/list.json?count=15&page=2'
    r = requests.get(url, headers=get_headers())
    sm_list=r.json()['result']['list']
    list_num=len(sm_list)
    for i in range(0,3):
        smid = r.json()['result']['list'][i]['smid']
        user_nick = r.json()['result']['list'][i]['user']['nick']
        like = r.json()['result']['list'][i]['liked']
        topic_name = r.json()['result']['list'][i]['topic']['name']
        topic_suid = r.json()['result']['list'][i]['topic']['suid']
        postition = {
            '视频ID': smid,
            '吧名': topic_name,
            '用户昵称': user_nick,
            '视频点赞数': like,
            '吧ID': topic_suid
        }
        if postition:
            postitions.append(postition)

        else:
            print('postition的值是None')
            # print('else里的值是postition',postition)
    return postitions

    # print('like=',like)
    # print('smid=',smid)
    # print('user_nick=',user_nick)
    # print('topic_name=',topic_name)
    # print('topic_suid=',topic_suid)
    # print('topic_suid=',topic_suid2)

def writecsv():
    headers={'视频ID','吧名','用户昵称','视频点赞数','吧ID'}
    for i in range(1,10):
        postition=onSwipe()
        with open('kuai8.csv','a',newline='',encoding='gbk') as f:
            write=csv.DictWriter(f,headers)
            write.writeheader()
            write.writerows(postition)
writecsv()