import requests
def get_headers():
    headers = {
        'User-Agent': 'kuai8shi pai/1.1.3 (iPhone; iOS 12.1.4; Scale/2.00)',
        'cp-abid': '2-100',
        'cp-appid': '800',
        'cp-sign':'ea65b8e0cc487cb42039e9c1f5efa820',
        'cp-ver': '1.1.3',
        'cp-token': 'eZ3AHVbYv0Y1nnq5S2aMkYSU3nK8lz8A9Sll0EwFjjo_',
        'cp-os':'ios',
        'cp - vend': 'kuai8',
        'cp - oem': 'iphone8',
        'AppKey': 'kuai8-ios'
    }
    return headers

def get_token(phoneNum=18810037430):
    r = requests.get(
        url='http://dev.api.kuai8.mobi/1/user/bindphone.json?captcha=6868&phone=%s'%(str(phoneNum)),
        headers=get_headers(),
    )
    token=r.json()
    token=token['result']['token']
    return token
get_token()
