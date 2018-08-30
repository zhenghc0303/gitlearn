from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import time

class Spider:


    #定义一个爬取网页数据的方法
    def get_url(self, url):
        usr_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        web_headers = {'User-Agent': usr_agent}
        content = requests.get(url, headers = web_headers).text
        return  content
    #定义一个自动获取贴子页数，并构建网页列表的方法
    def url_lst(self, url_p):
        content = self.get_url(url_p)
        re_page = re.compile(r'<span class="red">(.*?)</span>', re.S)
        page_number = re_page.findall(content)
        pag = int(page_number[0])
        url_lst = []
        for num in range(1,pag+1):
            urls = (url_p+'?pn={}'.format(num))
            url_lst.append(urls)
        return url_lst
    #定义一个利用BeautifulSoup获取网页图片链接并保存为列表的方法
    def bs_pattren(self, url):
        bs_pattren = BeautifulSoup(self.get_url(url))
        img_lst = bs_pattren.find_all('img', attrs={'class':'BDE_Image'})
        link_lst = []
        for iterm in img_lst:
            link = iterm['src']
            link_lst.append(link)
        return link_lst

    #定义一个下载图片的方法
    def bian_li(self,url):
        url_lst = self.url_lst(url)
        for url in url_lst:
            link_lst = self.bs_pattren(url)
            x = 1
            for link in link_lst:
                print('第{}张'.format(x),link)
                #使用urllib下载链接，并保存
                urllib.request.urlretrieve(link, r'D:\image\第{}张{}'.format(x, link[-6:]))
                x += 1
        time.sleep(1)
        urllib.request.urlcleanup()





tie_num = str(input('请输入帖子号：'))
urls = 'http://tieba.baidu.com/p/{}'.format(tie_num)

zhua_qu = Spider()
lst = zhua_qu.bian_li(urls)

'''
需要注意的是
1、类中调用自身方法时，使用self.funcation()。调用自身属性时，使用self.name
2、正则表达式中.*和.*?的区别是,不加?号匹配最长的字符串，加?号表示匹配最短的字符串
3、BeautifulSoup对页面进行find_all方法时，到最后一级的时要使用[]进行索引，如找到所有div时用find_all
    要找到‘div’中的‘img’时用find_all,找’img‘中的’src‘时要用[]。
'''
