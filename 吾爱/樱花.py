#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/5/27 22:03
#@File  : 樱花.py
import os
import requests
from lxml import etree
import re
import json
import time
 
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59',
     
}
#保存文件
def xzwj(xz,head,path):
    w_na = xz.split("/")[-1]    #拆分地址，以最后一段为存盘的文件名
#     print(w_na)
    w_rar = requests.get(xz,headers=head).content
    with open(path+f'//{w_na}','wb') as f:   #修改e://debug//  处，改变文件存放位置。文件目录必须提前建好。
        f.write(w_rar)
        print("正在下载，请耐心等待。。。")
        print(w_na,"下载完成")
 
#解释压缩文件网址
def rar_xz(rar_url,head):
    xz_res = requests.get(rar_url,headers=head).text
    xz_rar = re.compile(r'window.location=\'(.*?)\'')
    xz = xz_rar.findall(xz_res)[0]
#     print(xz_res)
#     print(xz)
    return xz
 
def xzxz(xx):   #文件下载
    print("要下载的内容和网址是：",pna[xx-1],pli[xx-1])
    print("---------开始下载展示图片------------")
    r_resp = requests.get(pli[xx-1],headers=headers)
    r_tree = etree.HTML(r_resp.text)
    r_imgs = r_tree.xpath('//div/div/p/img/@src')   #获取每张图片的网址
    r_nas = r_tree.xpath('//div/div/p/img/@title')  #获取下载的图片的文件名
    rar_url = r_tree.xpath('//div/div[@class="pay-box"]/a/@href')[0]  #获取下载文件的网址
    # print(rar_url)
    # print(len(r_nas),len(r_imgs))
    # print(r_nas,r_imgs)
    n=1
    path = f"e://debug//{r_nas[0]}"
    if not os.path.exists(path):
        os.mkdir(path)
    head ={
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59',
        'referer':pli[xx-1]
    }
    for img in r_imgs:
    #     print(img)
        xzwj(img,head,path)
        print(f"{r_nas[0][:-2]},第{n}张下载完成---")
        n += 1
    print("共",len(r_imgs),"张下载完成")
    print("==============开始下载压缩文件============")
    xz = rar_xz(rar_url,head)
    xzwj(xz,head,path)
 
def main_xz():    
    print("1.性感美女 2.清纯可爱 3.性感御姐 4.制服诱惑")
    ms = input("请选择分类：")
    url1 = "https://dimgw.us/xinggan"
    url2 = "https://dimgw.us/qc"
    url3 = "https://dimgw.us/yj"
    url4 = "https://dimgw.us/zf"
    if int(ms) == 1:
        url = url1
    elif int(ms) == 2:
        url = url2
    elif int(ms) == 3:
        url = url3
    elif int(ms) == 4:
        url = url4
    # print(url)
    resp = requests.get(url,headers=headers)
    pages = re.findall(r'<a class="page-numbers" href="(.*?)</a>',resp.text)[-1]
    #print(resp.status_code)
    page = pages.split(">")[-1]
    print("此类共",page,"页！")
    print("*"*50)
    pna = []
    pli = []
    for p in range(1,int(page)+1):
        purl = url + f"/page/{p}"
        presp = requests.get(purl,headers=headers)
        tree = etree.HTML(presp.text)
        rw_li = tree.xpath('//div[@class="row posts-wrapper"]//div/a[@target="_blank"]/@href')
        rw_na = tree.xpath('//div[@class="row posts-wrapper"]//div/a[@target="_blank"]/img/@alt')
        # print(rw_na)2
 
        pna.extend(rw_na)
        pli.extend(rw_li)
    print("-"*50,"\n","共有以下美女可选：")
    for na in pna:
        print(pna.index(na)+1,na)
    return pna,pli
 
pna,pli = main_xz()
var = 1
while var != len(pna):
    xx = int(input("请输入要下载的序号(0退出):"))
    if xx != 0:
        xzxz(xx)
    else:
        print("退出")
        break
    var +=1