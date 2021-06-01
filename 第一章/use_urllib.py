#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 爬虫: 通过编写程序来获取到互联网上的资源
# 百度
# 需求: 用程序模拟浏览器. 输入一个网址. 从该网址中获取到资源或者内容
# python搞定以上需求. 特别简单
import io
import sys
from urllib import request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
resp = request.urlopen("http://www.baidu.com/")
with open("baidu.html", mode="w",encoding='utf-8') as f:
    #print(resp.read().decode("utf-8"))
    f.write(resp.read().decode("utf-8"))  # 读取到网页的页面源代码
print("over!")