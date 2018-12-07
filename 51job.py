# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

class Spider():

    def url_get(self, url):
        text = requests.get(url , headers = webheader).content
        return text

    def page_list(self, page):
        text = self.url_get(page)
        bs_info = BeautifulSoup(text, 'html.parser')
        div = bs_info.find_all('div', {'class': 'rt'})
        page_num = div[1].text[-2]
        page_ls = []
        for n in range(1,int(page_num)+1):
            page_url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(searchs, n)
            page_ls.append(page_url)
        print('总共有{}页'.format(len(page_ls)))
        return page_ls

    def cont_get(self, url):
        url_ls = self.page_list(url)
        con_ls = []
        p = 1
        for url_num in url_ls:
            print('第{}页'.format(p))
            bs_info = BeautifulSoup(self.url_get(url_num), 'html.parser')
            t1 = bs_info.find_all('p', attrs={'class': 't1'})
            t2 = bs_info.find_all('span', attrs={'class': 't2'})
            t3 = bs_info.find_all('span', attrs={'class': 't3'})
            t4 = bs_info.find_all('span', attrs={'class': 't4'})
            t5 = bs_info.find_all('span', attrs={'class': 't5'})
            del (t2[0])
            del (t3[0])
            del (t4[0])
            del (t5[0])
            p += 1

            for i in range(0, len(t2)):
                s = '职位名：' + t1[i].text.strip() + '\n' + '公司名：' + t2[i].text.strip() + '\n' + '工作地：' + \
                    t3[i].text.strip() + '\n' + '薪资  ：' + t4[i].text.strip() + '\n' + '时间  ：' + t5[i].text.strip() + '\n'
                con_ls.append(s)

        with open(r'D:\{}.txt'.format(searchs), 'a+', encoding='utf8') as f:
            u = 1
            for cont in con_ls:
                nei = str(u) + '\n' + cont
                f.write(nei)
                u += 1
            print('共有{}条招聘信息。'.format(u)  + '\n' + '完成抓取')
            f.close()


searchs = str(input("请输入关键字："))
url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(searchs)
webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

job_search = Spider()
job_search.cont_get(url)