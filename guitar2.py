import requests
from selenium import webdriver
import xlrd
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
# 设置为开发者模式，避免被识别
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)
driver.maximize_window()
data = xlrd.open_workbook('guitar.xlsx')
table = data.sheets()[0]
links = table.col_values(int(2))
for url in links[1:]:
    try:
        driver.get(url)
    except Exception as e:
        print(e)
    wait = WebDriverWait(driver, 2, 0.2)  # 设置等待时间
    imgs = driver.find_elements_by_xpath(
        '//*[@class="single_content the_content zhengwen"]/p/img')
    title = driver.find_element_by_xpath('//*[@class="shipin-title"]').text
    print(title)
    n = 1
    for i in imgs:
        url = i.get_attribute('src')
        r = requests.get(url)
        # 将获取到的图片二进制流写入本地文件
        with open(f"qupu/{title}+{n}.jpg", 'wb') as f:
            # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
            f.write(r.content)
            print("下载成功!")
        n += 1