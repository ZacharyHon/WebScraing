"https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# window.asrsea(JSON.stringify(i2x), bwa1x(["流泪", "强"]), bwa1x(RQ7J.md), bwa1x(["爱心", "女孩", "惊恐", "大笑"]));
# params = encText, encSeckey = encSeckey
# "rid=R_SO_4_254260&threadId=R_SO_4_254260&pageNo=1&pageSize=20&cursor=-1&offset=0&orderType=1"
# pip install pycrypto

from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_254260",
    "threadId": "R_SO_4_254260",
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7 "
g = "0CoJUm6Qyw8W8jud"
i = "QQJ2Fa7zlCZKpxbE"


def get_encSecKey():
    return "5ec3b6ce01a47dc47ee75411efb8bbb4e35436ebd69050daef22891daa0067f1e03305d31e2ddfc63e5ee3b5c1e2e26bce45d1b2bc5ac0adf4a561ad0c8247037755acec1bc6c335e961ef7cc6600d5fb598fd8cbd90d7297b11c1206ddb272303d45cc0c1a74bbf6c3820309b32cf5541b6192d144bf79cac323db9e540a665 "


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    byte_string = aes.encrypt(data.encode("utf-8"))  # 加密
    return str(b64encode(byte_string), "utf-8")


"""
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
"""
# 处理加密过程
"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),       // 两次加密 第一次将数据与g加密 第二次将新的数据与随机i加密
        h.encSecKey = c(i, e, f),
        h
    }
     window.asrsea = d    // d是data, e是010001 f很长 g是0CoJUm6Qyw8W8jud
"""

resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.text)
