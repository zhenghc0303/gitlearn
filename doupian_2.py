#! /usr/bin/python3
# coding:utf-8

import time
import requests
from bs4 import BeautifulSoup

#创建请求报头和网址列表
page_num = 1
urls= []
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
for a in range(90):
    url = 'https://movie.douban.com/tag/%E7%83%82%E7%89%87?start={}&type=T'.format(a * 20)
    urls.append(url)

#抓取网页的源代码，并返回为Beautifulsoup格式
for ur in urls:
    print('第{}页'.format(page_num))
    page_num += 1
    page = requests.get(ur, headers=webheader ).text
    bs_page = BeautifulSoup(page, 'html.parser')
    #按要求找到所有符合要求内容相对应的标签和属性值
    tags = bs_page.find_all('div', attrs={'class':'pl2'})
    #遍历标签，在每一个div中找到需要的信息
    try:
        for tag in tags:
            #找到div标签下第一个a标签的文本内容。
            name = tag.find('a').get_text().replace(' ','').strip('\n').replace('\n','')
            #找到div标签下第一个’p‘标签的文本内容
            actor = tag.find('p').get_text().replace(' ','').strip('\n').replace('\n','')
            #找到div标签下第一个div标签下的所有’span‘标签列表中的第一个和第二个元素的文本内容
            rate = tag.find('div').find_all('span')[1].get_text()
            number = tag.find('div').find_all('span')[2].get_text()[1:-1]
            #将找出来的信息综合后写入文本文件
            all = name + '；' + '\n'+actor + '；'+ '\n' + rate +'分；' +number + '。' + '\n' + '=' * 100 + '\n'
            with open('douban.txt', 'a+' ,encoding='utf8') as f:
                f.write(all)
            #设置程序运行间隔时间
            time.sleep(1)
    except:
        continue
print('done')
