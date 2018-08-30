import requests
import re
import time

url = 'https://www.qiushibaike.com/'
#获取网页源代码
def get_url(url):
    usr_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    web_head = {'User-Agent':usr_agent}
    req = requests.get(url, headers= web_head)
    content = req.text
    return content

conrent = get_url(url)
#正则匹配代码
def get_re(content):
    #正则表达式，后面的re.S指将字符串中的换行符按照\n输出，整段匹配，而不是整行匹配
    re_pattern = re.compile('<div class="author.*?<h2>(.*?)</h2>.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span.*?stats-vote.*?number">(.*?)</i>.*?stats-comments.*?number">(.*?)</i>.*?up.*?number hidden">(.*?)</span>.*?down.*?number hidden">(.*?)</span>',re.S)
    #匹配代码
    details = re_pattern.findall(content)
# 数据清洗
    def replace(x):
        qx = re.sub(re.compile('<br>|</br>|/>|<br'), "", x)
        return qx.strip()
    #将内容循环打印输出
    number = 1
    for detial in details:
        te_xt = '\n'+str(number) +'楼' + '\n楼主：' + detial[0]+''+detial[1]+'岁'+'\n发言:'+replace(detial[2])+'\n好笑：'+detial[3]+'\n评论：'+detial[4]+'\n赞：'+detial[5]+'\n踩：'+detial[6]
        time.sleep(0.1)
        number += 1
        with open('qiu_shi.txt', 'a+', encoding='utf-8') as f:
            f.write(te_xt)
    f.close()

get_re(conrent)