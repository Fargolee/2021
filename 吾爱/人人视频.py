'''
Author: Lee
Descripttion: Myhome
Date: 2022-05-28 22:18:32
'''
#windows 10 Python 3.6 x86
import requests
import json
import re
import os
from concurrent.futures import ThreadPoolExecutor
headers = {
'Referer':'https://m.rr.tv/',#全局设置
'User-Agent':'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'
}
vod_list = []#存储视频链接
vod_name = []#存储视频标题
get_down_url =[]#存储下载直链
def get_vod(url):
    response = requests.get(url = url,headers = headers)#请求url
    vod_list.append(re.findall(re.compile(r'data:\[{id:(.*?),title:"'),response.text)[0])#找找视频链接
    vod_name.append(re.findall(re.compile(r',title:"(.*?)",desc:"'),response.text)[0])#找找视频标题
    for i in re.findall(re.compile(r'{sid:"(.*?)",key:'),response.text):
        url ="https://web-api.rr.tv/web/drama/play?webChannel=M_STATION&dramaId="+vod_list[0]+"&episodeId="+i+"&2-7-17xx"#拼接地址
        response = requests.get(url = url,headers = headers)
        get_down_url.append(str(json.loads(response.text)['data']['url']))#拿下载直链进list
def down_begin(url,i):
        print("开始多线程下载"+vod_name[0]+"第"+str(i)+"集")
        r = requests.get(url = url,headers = headers)#下载请求
        f = open("./"+vod_name[0]+"/第"+str(i)+"集.MP4", "wb")#保存视频
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
if __name__ == '__main__':
    url='https://m.rr.tv/detail/xxxxx?snum=1&episode=1'#进入rr.tv自行获取
    get_vod(url)
    os.mkdir('./'+vod_name[0])#创建视频保存目录
    with ThreadPoolExecutor(10) as f:#这里写多线程参数，适合几十集的电视剧使用
        for i,url in enumerate(get_down_url):
            i=int(i)+1
            f.submit(down_begin,url = url,i=i)