'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-13 16:22:59
'''
import requests
import json
import re
 
 
# 定义保存评论的函数
def bcpl(weibo_id, url, headers, number):
    count = 0    #设置一个初始变量count为0来进行计数
    with open("微博id" + str(weibo_id) + ".txt", "a", encoding="utf8") as f:    #打开一个名为“微博idxxxxxx”的txt文件，编码utf-8
    # 当count数量小于预期的number时，进行循环
        while count < number:
            # 判断是不是第一组评论，如果是的话，第一组评论不需要加max_id，之后的需要加
            if count == 0:
                try:
                    url = url + weibo_id + '&mid=' + weibo_id + '&max_id_type=0'
                    web_data = requests.get(url, headers=headers)    #F12查看data信息
                    js_con = web_data.json()    #转换一下数据格式
                    # 获取连接下一页评论的max_id
                    max_id = js_con['data']['max_id']  #max_id在[data]中
                    print(max_id)
                    comments = js_con['data']['data']    #获得数据中[data]中的[data]
                    for comment in comments:    #依次循环获得comments中的数据
                        comment = comment["text"]     #获得[text]下的数据，也就是评论数据
                        label = re.compile(r'</?\w+[^>]*>', re.S)    #删除表情符号
                        comment = re.sub(label, '', comment)    #获得文本评论
                        f.write(comment + '\n')    #写入到文件中
                        count += 1    #count = count + 1
                        print("已爬取" + str(count) + "条评论！"  ) #显示爬取到第几条
                except Exception as e:
                    print("出错了" ,e)
                    continue
            else:
                try:
                    url = url + weibo_id + 'max_id=' + str(max_id) + '&max_id_type=0'
                    web_data = requests.get(url, headers=headers)
                    js_con = web_data.json()
                    max_id = js_con['data']['max_id']
                    comments = js_con['data']['data']
                    for comment in comments:
                        comment = comment["text"]
                        label = re.compile(r'</?\w+[^>]*>', re.S)
                        comment = re.sub(label, '', comment)
                        f.write(comment+ '\n')
                        count += 1
                        print("已爬取" + str(count) + "条评论！")
                except Exception as e:
                    print("出错了" ,e)
                    continue
 
 
 
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }    #设置user-agent来进行伪装，突破微博反爬限制
    url = 'https://m.weibo.cn/comments/hotflow?id='
    weibo_id = '4478512314460101'  # 要爬取的微博id  #[url=https://m.weibo.cn/detail/4478512314460101]https://m.weibo.cn/detail/4478512314460101[/url]
    #打开微博手机端网页[url=https://m.weibo.cn]https://m.weibo.cn[/url]，找到要爬取的微博id！
    #手机端网页！手机端网页！手机端网页！
    number = 60000 # 设置爬取评论量,爬取量在第X组，爬取时会爬取下来该组的数据，所以最终数据可能会大于number，一般是个整10的数
    bcpl(weibo_id, url, headers, number)