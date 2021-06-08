import multiprocessing

import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import Process
import ssl


def get_url():
    dts = []
    for i in range(1, 256):
        u = 'https://www.jitatang.com/pu/page/' + str(i)
        html = requests.get(
            u, headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
            timeout=30)  # 获取网页
        soup = BeautifulSoup(
            html.content,
            "lxml",
            from_encoding='utf-8')  # 获取lxml树
        urls = soup.find_all('div', attrs={'class': 'index-pu-meta'})
        ssl._create_default_https_context = ssl._create_unverified_context
        for url in urls:
            lst = []
            b = url.find('a').get('href')
            title = url.find('a').get('title')
            lst.append(title)
            lst.append(b)
            dts.append(lst)
        df = pd.DataFrame(dts, columns=['title', 'urls'])
    df.to_excel('guitar.xlsx', encoding='utf-8')


if __name__ == '__main__':
    multiprocessing.Process(target=get_url).start()
    process_list = []
    for i in range(1, 256):
        url1 = 'https://www.jitatang.com/pu/page/' + str(i)
        p1 = Process(target=get_url, args=(url1,))
        p1.start()
    for i in range(101, 256):
        url2 = 'https://www.jitatang.com/pu/page/' + str(i)
        p2 = Process(target=get_url, args=(url2,))
        p2.start()
    for i in range(101, 151):
        url3 = 'https://www.jitatang.com/pu/page/' + str(i)
        p3 = Process(target=get_url, args=(url3,))
        p3.start()

    for i in range(151, 256):
        url4 = 'https://www.jitatang.com/pu/page/' + str(i)
        p4 = Process(target=get_url, args=(url4,))
        p4.start()
    process_list.append(p1)
    process_list.append(p2)
    process_list.append(p3)
    process_list.append(p4)
    for t in process_list:
        t.join()
