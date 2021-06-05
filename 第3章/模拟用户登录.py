# 登录 -> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容

import requests

# 会话
session = requests.session()

data = {
    "loginName": "15849181913",
    "password": "HZH20000506"
}
# 1.登录

url = " https://passport.17k.com/ck/user/login"

resp = session.post(url, data=data)

print(resp.text)
