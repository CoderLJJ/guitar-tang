import multiprocessing

import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import Process
import ssl

from lxml import etree

list =[]
for i in range(1,56):
    url = 'https://www.jitatang.com/video/page/'+str(i)
    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.content,"lxml",from_encoding='utf-8')  # 获取lxml树
    titles =soup.select('div.index-video-title > a')
    for t in titles:
        s = []
        title = t.get('title')
        url = t.get('href')
        print(title,url)
        s.append(title)
        s.append(url)
        list.append(s)
    df = pd.DataFrame(list, columns=['title', 'urls'])
df.to_excel('guitar-video.xlsx', encoding='utf-8')