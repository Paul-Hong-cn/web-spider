import requests
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
for i in range(0, 10):
    page = i * 25
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    content_all = soup.find_all(class_='pic')
    for content in content_all:
        imgContent = content.find(name='img')
        imgName = imgContent.attrs['alt']
        imgUrl = imgContent.attrs['src']
        imgUrlHd = imgUrl.replace('s_ratio_poster', 'm')
        imgResponse = requests.get(imgUrlHd)
        img = imgResponse.content
        with open(f'{imgName}.jpg', 'wb') as f:
            f.write(img)
        print(f"downloaded:{imgName}")