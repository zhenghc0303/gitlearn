#! /usr/bin/python3
#coding:utf-8

import urllib.request
import re
import os

targetDir = r'D:\Pythonwork\load'
def destFile(path):
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex(r'/')
    t = os.path.jion(targetDir, path[pos+1:])
    return t
#创建网址分页列表和请求报头
urls = ['http://www..html']
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
for y in range(2,14):
    urls.append('http://3918_{}.html'.format(y))

x = 1
for url in urls:
    #利用urllib发送网址请求
    req = urllib.request.Request(url=url,headers=webheader)
    #利用urllib打开网址
    webPage = urllib.request.urlopen(req)
    #利用urllib读取网页内容
    data = webPage.read()
    #用正则表达式找到所有的图片链接
    for link, t in set(re.findall(r'(http:[^\s]*?-\d?\d?.(jpg))',str(data))):
        print(link)
        try:
            #利用urllib下载图片链接的内容，保存为JPG格式，保存到本地文件夹链接
            urllib.request.urlretrieve(link, r'C:\Users\xueshu\PycharmProjects\A 111\Loda\看0{}图片0{}'.format(x,link[-14:]))
            x += 1
        except:
            print('error')
        print('di',x, 'ye')
#清除所有的urllib缓存
urllib.request.urlcleanup()
hhhead = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
            }
