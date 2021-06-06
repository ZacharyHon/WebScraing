"https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# window.asrsea(JSON.stringify(i2x), bwa1x(["流泪", "强"]), bwa1x(RQ7J.md), bwa1x(["爱心", "女孩", "惊恐", "大笑"]));
# params = encText, encSeckey = encSeckey
# "rid=R_SO_4_254260&threadId=R_SO_4_254260&pageNo=1&pageSize=20&cursor=-1&offset=0&orderType=1"
# pip install pycrypto
import csv

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

# print(resp.json())

f = open(f"孤单北半球.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)

comments = resp.json()["data"]["comments"]  # 获取每个的评论记录
for comment in comments:
    user = comment['user']  # 用户记录
    userId = user['userId'] # 用户Id
    nickname = user['nickname']  # 用户昵称
    avatarUrl = user['avatarUrl']
    content = comment['content']  # 获取评论内容
    beReplied_comment = comment['beReplied']  # 是否是追评，是的话值为原评论人的信息，否为None
    csvwriter.writerow([userId, nickname, content])
    if beReplied_comment is not None:
        beReplied_user = beReplied_comment[0]['user']
        beReplied_userId = beReplied_user['userId'] # 用户Id
        beReplied_nickname = beReplied_user['nickname']  # 用户昵称
        beReplied_avatarUrl = beReplied_user['avatarUrl']
        beReplied_content = beReplied_comment[0]['content'] # 获取评论内容
        csvwriter.writerow([beReplied_userId,beReplied_nickname,beReplied_content])

print('over!')

# {'code': 200, 'data': {'comments': [{'user': {'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None,
#                                               'liveInfo': None, 'followed': False, 'vipRights': None,
#                                               'relationTag': None, 'anonym': 0, 'userId': 1442636111, 'userType': 0,
#                                               'nickname': '满满牌芋泥奶露',
#                                               'avatarUrl': 'https://p1.music.126.net/hOv7Cha-lv10RKzopJEEjg==/109951165966910895.jpg',
#                                               'authStatus': 0, 'expertTags': None, 'experts': None, 'vipType': 0,
#                                               'remarkName': None, 'isHug': False}, 'beReplied': [{'user': {
#     'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None, 'liveInfo': None, 'followed': False,
#     'vipRights': None, 'relationTag': None, 'anonym': 0, 'userId': 19712407, 'userType': 0, 'nickname': '小撸猫',
#     'avatarUrl': 'https://p1.music.126.net/73vbfT3clBs_sPT2ZEAZZw==/3242459790535318.jpg', 'authStatus': 0,
#     'expertTags': None, 'experts': None, 'vipType': 0, 'remarkName': None, 'isHug': False},
#                                                                                                   'beRepliedCommentId': 13040982,
#                                                                                                   'content': '这歌是Flash流行的年代，听到这歌有一种想哭的感觉。',
#                                                                                                   'status': 0,
#                                                                                                   'expressionUrl': None}],
#                                      'commentId': 5325303608, 'content': '15年的评论了……', 'status': 0,
#                                      'time': 1622915906183, 'likedCount': 0, 'liked': False, 'expressionUrl': None,
#                                      'parentCommentId': 13040982, 'repliedMark': False, 'pendantData': None,
#                                      'showFloorComment': {'replyCount': 0, 'comments': None, 'showReplyCount': False,
#                                                           'topCommentIds': None, 'target': None},
#                                      'decoration': {'repliedByAuthorCount': 0}, 'commentLocationType': 0, 'args': None,
#                                      'tag': {'datas': None, 'relatedCommentIds': None}, 'source': None, 'extInfo': {},
#                                      'commentVideoVO': None}, {
#                                         'user': {'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None,
#                                                  'liveInfo': None, 'followed': False, 'vipRights': None,
#                                                  'relationTag': None, 'anonym': 0, 'userId': 4004694072, 'userType': 0,
#                                                  'nickname': '未来可期_bfZR',
#                                                  'avatarUrl': 'https://p1.music.126.net/76eNFFlmIMyUxIaLV9MUKA==/109951166045189211.jpg',
#                                                  'authStatus': 0, 'expertTags': None, 'experts': None, 'vipType': 0,
#                                                  'remarkName': None, 'isHug': False}, 'beReplied': [{'user': {
#         'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None, 'liveInfo': None, 'followed': False,
#         'vipRights': None, 'relationTag': None, 'anonym': 0, 'userId': 1946268782, 'userType': 0, 'nickname': '也许是珊瑚',
#         'avatarUrl': 'https://p1.music.126.net/a-J7F7kCZF0zjSEJTi0n4Q==/109951165117263384.jpg', 'authStatus': 0,
#         'expertTags': None, 'experts': None, 'vipType': 0, 'remarkName': None, 'isHug': False},
#                                                                                                      'beRepliedCommentId': 5269845737,
#                                                                                                      'content': '异地恋真的好辛苦',
#                                                                                                      'status': 0,
#                                                                                                      'expressionUrl': None}],
#                                         'commentId': 5324071878, 'content': '异国恋呢？', 'status': 0, 'time': 1622774146802,
#                                         'likedCount': 0, 'liked': False, 'expressionUrl': None,
#                                         'parentCommentId': 5269845737, 'repliedMark': False, 'pendantData': None,
#                                         'showFloorComment': {'replyCount': 0, 'comments': None, 'showReplyCount': False,
#                                                              'topCommentIds': None, 'target': None},
#                                         'decoration': {'repliedByAuthorCount': 0}, 'commentLocationType': 0,
#                                         'args': None, 'tag': {'datas': None, 'relatedCommentIds': None}, 'source': None,
#                                         'extInfo': {}, 'commentVideoVO': None}, {
#                                         'user': {'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None,
#                                                  'liveInfo': None, 'followed': False, 'vipRights': None,
#                                                  'relationTag': None, 'anonym': 0, 'userId': 4004694072, 'userType': 0,
#                                                  'nickname': '未来可期_bfZR',
#                                                  'avatarUrl': 'https://p1.music.126.net/76eNFFlmIMyUxIaLV9MUKA==/109951166045189211.jpg',
#                                                  'authStatus': 0, 'expertTags': None, 'experts': None, 'vipType': 0,
#                                                  'remarkName': None, 'isHug': False}, 'beReplied': [{'user': {
#         'avatarDetail': None, 'commonIdentity': None, 'locationInfo': None, 'liveInfo': None, 'followed': False,
#         'vipRights': None, 'relationTag': None, 'anonym': 0, 'userId': 4890405952, 'userType': 0,
