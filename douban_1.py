#! /usr/bin/python3
#coding:utf-8

import requests
from bs4 import  BeautifulSoup

url = 'https://movie.douban.com/chart'
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

reponse = requests.get(url, headers = webheader).text
#获取网页源代码
bsobj = BeautifulSoup(reponse, 'html.parser')
# 将网页源代码转换成Beautifulsoup对象
bsobj = bsobj.find_all('div', attrs={'class':'pl2'})
# .find_all()函数找出Beautifulsoup对象中所有符合要求的标签：
#有两个参数，第一个参数是标签的名字，第二个参数是标签的属性
for tag in bsobj:
    div_tag = tag.contents[1].get_text()
    # tag.contents 将 tag 转化为列表格式，以便于索引第一个内容后获取标签<...>..<\...>之间的文本内容
    #如果没有tag.contents[1],返回的是tag中所有标签的文本内容，而我们只需要第一个标签里的文本内容
    #print(div_tag)
    name = div_tag.replace(' ', '').strip('\n')
    # .replace(' ', '')操作字符串，将字符串中的元素替换
    # .strip('\n')操作字符串，将字符串两端的换行符去掉
    print(name)
    print('=' * 100)
