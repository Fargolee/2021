'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-13 16:04:42
'''
import requests
import re
import time
from lxml import etree
 
 
 
 
def cczh(str):    #定义一个尺码转换函数，不同的尺寸转换为A/B/C/D/E
    if 'E' in str:   #如果数据中有E则：
        return 'E'   #返回E
    if 'D' in str:
        return 'D'
    if 'C' in str:
        return 'C'
    if 'B' in str:
        return 'B'
    if 'A' in str:
        return 'A'
    if 'XXL' in str:
        return 'E'
    if 'XL' in str:
        return 'D'
    if 'L' in str:
        return 'C'
    if 'M' in str:
        return 'B'
    if 'S' in str:
        return 'A'
    if '均码' in str:
        return 'B'
    if '大' in str:
        return 'C'
    if '小' in str:
        return 'A'
 
 
 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}    #设置一个请求头来突破反爬
 
 
all_sizes = []    #用一个空列表all_sizes来准备装尺寸数据
"""获得商品id"""
for i in range(1,51):    #依次生成1-50来进行网址拼接
    #拼接网址
    url = "https://list.jd.com/list.html?cat=1315,1345,1364&ev=exbrand_90320&page=" + str(i) + "&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    res = requests.get(url,headers=headers).text    #用requests的get函数来获取信息，用headers=headers来进行伪装.text转换为文本信息
    res_xpath = etree.HTML(res)    #转换为xpath类型
    sp_ids = res_xpath.xpath('//*[@id="plist"]/ul/li/div/@data-sku')   #用xpath提取商品的id
    time.sleep(5)   #设置5秒延时
    for sp_id in sp_ids:    #依次从sp_ids中提取sp_id来拼接
        """获得评论size"""
        for i in range(1,51):    #依次生成1-50来拼接评论网址
            url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId="+ str(sp_id) + "&score=0&sortType=5&page=" + str(i) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
            res = requests.get(url,headers=headers).text    #用requests的get函数来获取信息，用headers=headers来进行伪装.text转换为文本信息
            sizes = re.findall('"productSize":"(.*?)"',res)    #用正则表达式获得size信息
            print(sizes)   #打印一下尺寸信息
            for size in sizes:    #依次循环sizes中的信息
                all_sizes.append(size)    #将信息添加到all_sizes中
    time.sleep(5)    #设置5秒延时
 
"""进行尺码转换"""
abcds = []  #用一个空列表abcds准备装尺寸数据
for size in all_sizes:   #依次循环all_sizes中的信息
    size = cczh(size)  #用函数cczh来讲size的尺寸进行转换
    abcds.append(size)   #转换后的数据添加到abcds列表中
print(abcds)
print(len(abcds))   #查看尺寸总数量
 
"""进行尺寸统计"""
tjs = set(abcds)    #用列表abcds创建一个无序不重复元素集tjs，也就是删除重复元素，仅保留【A/B/C/D/E】等
for tj in tjs:    #依次从tjs中提取数据
    count = 0    #定义一个变量count=0进行计数
    for abcd in abcds:    #从abcds列表中依次提取数据
        if tj == abcd:    #如果abcd==tj则：
            count += 1    #count = count + 1   数量增加1
    print(tj, ": ", count)   #打印显示各个罩杯的数量