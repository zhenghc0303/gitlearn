#! /usr/bin/python3
# coding:utf-8

import requests

url = "http://www.baidu.com"
req = requests.get(url)
txt = req.text
print(txt)

