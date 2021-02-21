import requests, time, re, rsa, json, base64
from urllib import parse

s = requests.Session()

username = "6666666666"
password = "abxdhdhnfg"
a = "1"
b = "12"
c = "154"
d = "2"
e = "666"
f = "77"
g = "99"

if(username == "" or password == ""):
    username = input("账号：")
    password = input("密码：")

def main():
    rand = str(round(time.time()*1000))
    surl = f'https://api.cloud.189.cn/mkt/userSign.action?rand={rand}&clientType=TELEANDROID&version=8.6.3&model=SM-G930K'
    url = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN'
    url2 = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS&activityId=ACT_SIGNIN'
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G930K Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Ecloud/8.6.3 Android/22 clientId/355325117317828 clientModel/SM-G930K imsi/460071114317824 clientChannelId/qq proVersion/1.0.6',
        "Referer" : "https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1",
        "Host" : "m.cloud.189.cn",
        "Accept-Encoding" : "gzip, deflate",
    }
    if(a == b):
        print(f"未签到，签到获得M空间")
    else:
        if(a>c):
            print("哈哈哈哈哈")
        else:
            if(d>e):
                print(f"已经签到过了，签到获得M空间")
            else:
                print("呜呜呜呜")
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G930K Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Ecloud/8.6.3 Android/22 clientId/355325117317828 clientModel/SM-G930K imsi/460071114317824 clientChannelId/qq proVersion/1.0.6',
        "Referer" : "https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1",
        "Host" : "m.cloud.189.cn",
        "Accept-Encoding" : "gzip, deflate",
    }
    if (f > g):
        print("f>g???")
    else:
        if(a == b):
            print(f"未签到，签到获得M空间")
        else:
            if(a>c):
                print("哈哈哈哈哈")
            else:
                if(d>e):
                    print(f"已经签到过了，签到获得M空间")
                else:
                    print("呜呜呜呜")

if __name__ == "__main__":
    main()
