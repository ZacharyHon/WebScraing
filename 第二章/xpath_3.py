# 拿页面源代码
# 提取和解析数据
import csv

import requests
from lxml import etree
kw = input("你想要查询的内容")
url = f'https://wuhan.zbj.com/search/f/?type=new&kw={kw}'

resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text)

f = open(f"{kw}.csv", mode="w",encoding='utf-8')
csvwriter = csv.writer(f)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')
    if price:
        price = price[0].strip("¥")
    else:  # 最下方有一个广告位
        continue
    title = kw.join(div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
    title = title.strip('"')
    company = div.xpath('./div/div/a[2]/div[1]/p/text()')[0]
    address = div.xpath('./div/div/a[2]/div[1]/div/span/text()')[0]
    csvwriter.writerow([title,price,company,address])
print("over!")
