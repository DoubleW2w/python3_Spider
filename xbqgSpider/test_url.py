# -*- coding: utf-8 -*-
# @Time     : 19:04
# @Author   : DoubleL2l
# @File     : test.py
# @Software : PyCharm
import random
import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

server = 'https://www.vbiquge.com/'
book_name = '诡秘之主.txt'
target = 'https://www.vbiquge.com/15_15338/'
hds = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Host': 'www.vbiquge.com',
    },
    {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'www.vbiquge.com',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
        'Host': 'www.vbiquge.com',
    }
]
headers = random.choice(hds)
req = requests.get(url=target, headers=headers)
req.encoding = 'utf-8'
html = req.text
# print(html)
chapter_bs = BeautifulSoup(html, 'lxml')
chapters = chapter_bs.find('div', id='list')
chapters = chapters.find_all('a')
# print(chapters[0])
# print(chapters[0].get('href'))
chapter_name = chapters[0].string
url = server + chapters[0].get('href')
print(url)
print(chapter_name)