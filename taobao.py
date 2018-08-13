#! /usr/bin/python3
# coding:utf-8

import requests
import json
import simplejson
import time

#构造请求报头和网址列表
header= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
urls = []
lst = [] #构建要写入文件的字符串列表

for y in range(1,20):
    ul = 'https://rate.tmall.com/list_detail_rate.htm?itemId=557652536444&spuId=874138264&sellerId=1999887296&order=3&currentPage={}'.format(y)
    urls.append(ul)
#遍历网址列表中的每一条网址
for url in urls:
    #抓包，并返回text文本
    resp = requests.get(url, headers = header).text[15:]
    #print(resp)
    #json中带s和不带s的区别，带s对象为文本，不带s对象为文件
    try:
        #将str类型的text格式字符串格式化为字典
        si_dict = simplejson.loads(resp)
        #将字典编码为json格式，其中indent参数为缩紧，将打印树形json结构，方便直观
        json_dict = json.dumps(si_dict, indent=2)
        #将json格式转化为Python对象
        dict = json.loads(json_dict)
        #print(type(dict['rateList'][0]))
        '''
        for v in dict['rateList']:
            print(v)
        '''
        #遍历json格式对象'rateList'键，值中列表的rateContent键值，rateContent键值即是淘宝评论内容，要抓取的东西
        for i in range(0,19):
            print(i) #打印遍历信息
            #print(dict['rateList'][i]['rateContent'])
            lst.append(str(i))  #将序号加入文本列表中
            lst.append(dict['rateList'][i]['rateContent']) #将评论内容加入文本列表中
            lst.append('追评:')
            try:
                #print('追评:')
                #print(dict['rateList'][i]['appendComment']['content'])
                lst.append(dict['rateList'][i]['appendComment']['content']) #将追评内容加入文本列表中
            except:
                continue
    except:
        continue
    #print(lst)
    time.sleep(1) #程序运行间隔为1秒
#遍历文本列表将，评论内容添加到文本文件中
for x in lst: 
    with open('content.txt', 'a+', encoding='utf8') as f: #'a+'指逐条添加内容到文本文件中
        f.write(x+'\n') #写入文件时加入换行符
