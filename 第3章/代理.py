import requests

# https://www.zdaye.com/FreeIPList.html

proxies = {
    "https": "https://113.100.209.81:3128"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
