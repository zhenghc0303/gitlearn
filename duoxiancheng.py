#! /usr/bin/python3
# coding:utf-8


import threading
import time
import requests
from bs4 import BeautifulSoup

#并发执行指单核心上一定时间内处理多个对象，并行指的是多核心同时处理多个对象
#同步指各个任务之间执行互为条件，不是单独执行。异步指各个任务之间没有联系，独立运行

#定义一个去除字符串中空白字符，换行符的方法
def format_str(s):
    return s.replace('\n', '').replace(' ','').replace('\t', '')

#定义一个方法，抓取页面中的书名与网址。
def get_urls_in_pages(from_page_num, to_page_num):
    #创建网址集合与请求报头
    urls = []
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    for i in range(from_page_num, to_page_num+1):
        urls.append('https://www.phei.com.cn/module/goods/searchkey.jsp?Page={}&Page=2&searchKey=计算机'.format(i))
    #创建一个包含所有页面所有书名网址的列表
    all_href_list = []
    for url in urls:
        #print(url)
        resp = requests.get(url, headers = header).text
        bs = BeautifulSoup(resp)
        a_list = bs.find_all('a') #找到网页中所有的’a‘标签
        needed_list = []  #创建一个本页面所有书名网址的列表
        for a in a_list:
            #筛选出所有有网址的’a‘标签
            if 'href' in a.attrs:
                href_val = a['href']
                title = a.text
                #筛选出网址中符合要求的网址
                if 'bookid' in href_val and 'shopcar0.jsp' not in href_val and title != '':
                    #判断书名与网址是否已经添加到本页面网址列表中，若不在则添加
                    if [title, href_val] not in needed_list:
                        needed_list.append([format_str(title), format_str(href_val)])
        #将本页面网址列表合并到所有页面网址列表中
        all_href_list += needed_list
    #将网址添加到文本文件中
    f = open('all_href.txt', 'w')
    for href in all_href_list:
        f.write('\t'.join(href) + '\n')
    f.close()
    print(from_page_num, to_page_num, len(all_href_list))

#定义多线程方法
def threading_text():
    #记录开始时间
    t1 = time.time()
    #定义列表，列表中的元素是元组，每个元组给出单一线程的参数
    page_range_list = [(1,10), (11,20), (21,30), (31,40)]
    #创建线程列表
    th_list = []
    #循环创建线程
    for page_range in page_range_list:
        #创建单一线程。Thread类有两个参数，target是现成的活动实体，后边是方法名称，不带（），带（）表示调用函数方法。
        #args参数的值必须为元组，当target引用的方法只有一个参数时，args应写成args= （args1，）的格式，否则会认为args= args1为整数
        th = threading.Thread(target=get_urls_in_pages,
                              args=(page_range[0], page_range[1]))
        #创建的线程添加到线程列表中，这里创建了四个线程
        th_list.append(th)
    #循环执行线程，异步并发的执行
    for th in th_list:
        th.star()
    #等待各线程执行完毕，循环退出外层函数
    for th in th_list:
        th.join()
    #记录结束时间
    t2 = time.time()
    print('使用时间 1：', t2-t1)
    return t2-t1
