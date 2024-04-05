import requests
from bs4 import BeautifulSoup
import time

count = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
def getPositionInfo(detail_url):
    global count
    res = requests.get(detail_url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    job = soup.find(class_='new_job_name').text
    companyName = soup.find(class_='com-name').string
    companyName = companyName.strip()
    position = soup.find(class_='job_position').string
    salary = soup.find(class_='job_money cutom_font').string
    salary = salary.encode()
    salary = salary.replace(b"\xee\x8b\xbf", b"0")
    salary = salary.replace(b"\xee\xa2\x9c", b"1")
    salary = salary.replace(b"\xee\x90\xb7", b"2")
    salary = salary.replace(b"\xee\x81\xa5", b"3")
    salary = salary.replace(b"\xee\xad\xb1", b"4")
    salary = salary.replace(b"\xee\xb2\xae", b"5")
    salary = salary.replace(b"\xef\x8a\x98", b"6")
    salary = salary.replace(b"\xef\x80\xa6", b"7")
    salary = salary.replace(b"\xee\xa1\xb1", b"8")
    salary = salary.replace(b"\xee\xbe\xad", b"9")
    salary = salary.decode()
    with open(r'D:\Python-3.12\VSCode\夜曲编程\职位数据.txt', 'a', encoding='utf-8') as f:
        f.write(job + "," + companyName + "," + position + "," + salary + "\n")
    count = count + 1
    print(f'downloaded-success:{count},page:{i}')

for i in range(1, 112):
    url = f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&area=&months=&days=&degree=&official=entry&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all(class_="title ellipsis font")
    for item in titles:
        detail_url = item.attrs["href"]
        getPositionInfo(detail_url)
    time.sleep(1)