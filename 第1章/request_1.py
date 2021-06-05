import requests

query = input("输入一个你喜欢的明星")

url = f'https://www.sogou.com/web?query={query}'

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 "
                  "Safari/537.36 "
}

resp = requests.get(url, headers=dic)  # 处理一个小小的反爬

with open(f"{query}.html", mode="w", encoding='utf-8') as f:
    f.write(resp.text)
resp.close()