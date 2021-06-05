import requests

url = "https://www.pearvideo.com/video_1731128"
contId = url.split("_")[1]

videoStatusUrl = "https://www.pearvideo.com/videoStatus.jsp?contId=1731128&mrd=0.25404975193663326"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    # 防盗链，溯源，即从哪里发起的请求？
    "Referer": url
}
resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]['videos']['srcUrl']
systemTime = dic['systemTime']
# 爬到的地址 https://video.pearvideo.com/mp4/adshort/20210602/1622730699106-15687219_adpkg-ad_hd.mp4
# 真实地址   https://video.pearvideo.com/mp4/adshort/20210602/cont-1731128-15687219_adpkg-ad_hd.mp4"

srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")

with open(f"mp4/{contId}.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

print("over!")

