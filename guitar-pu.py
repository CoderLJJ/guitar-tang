import multiprocessing
import os
import xlrd
import requests
from bs4 import BeautifulSoup


def get_url(url):
    html = requests.get(
        url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
        timeout=30)  # 获取网页
    soup = BeautifulSoup(
        html.content,
        "lxml",
        from_encoding='utf-8')  # 获取lxml树
    imgs = soup.find_all(
        'div', attrs={
            'class': 'single_content the_content zhengwen'})
    print(imgs)
    names = soup.find('h1', attrs={'class': 'shipin-title'}).text.replace('\\','').replace(' ','')
    print(names)
    for img in imgs:
        bb = img.find_all('img')
        print(bb)
        n = 1
        for b in bb:
            img = b.get('src')
            print(img)
            try:
                r = requests.get(img)
                path = f"qupu/{names}+{n}.jpg"
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(f'qupu/{names}{n}.png 下载完成!')
            except BaseException:
                print('error:')
            n += 1


if __name__ == '__main__':
      # 自动创建qupu文件夹
    if not os.path.exists('qupu'):
        os.mkdir('qupu')
    data = xlrd.open_workbook('guitar.xlsx')
    table = data.sheets()[0]
    links = table.col_values(int(2))
    for url in links[1:]:
        print(url)
    get_url('https://www.jitatang.com/67024.html')
