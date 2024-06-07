# 来吧，勇士！
# 导入requests模块
import requests
# 导入BeautifulSoup模块
from bs4 import BeautifulSoup
# 导入time模块
import time
# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd
# 导入random模块
import random
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
HousetypeList = []
AddressList = []
BuildinginformationList = []
PriceList = []
TotalList = []

# 将网页链接赋值给变量url
for page in range(1, 6):
    url = f"https://nocturne-spider.baicizhan.com/practise/61/PAGE/{page}.html"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        continue
    soup = BeautifulSoup(response.text, 'lxml')
# 获取每个房源的链接所在节点
    content_all = soup.find_all(class_="info clear")
# for循环便利content_all
    for content in content_all:
# 获取房屋户型，添加进对应的列表中
        title = content.find(class_="title").contents[1].string
        titles.append(title)
# 获取小区地址，添加进对应的列表中
        position = content.find(class_="positionInfo").a.string
        position_icons.append(position)
# 获取建筑楼层等信息，使用replace去掉换行，并添加进对应的列表中
        house = content.find(class_="houseInfo").contents[2].text.replace('\n','').replace('\r','')
        house_icons.append(house)
# 获取房屋总价，由于总价数值和单位在两个标签中，使用.text，并使用replace替换
        totalPrice = content.find(class_="totalPrice totalPrice2").text.replace('\n','').replace('\r','')
        total_prices.append(totalPrice)
# 获取房屋单价，添加进对应的列表中
        unitPrice = content.find(class_="unitPrice").span.string
        unit_price.append(unitPrice)
# 格式化输出每个数据，用逗号隔开
        print(f"{title},{position},{house},{totalPrice},{unitPrice}")
total = {"房屋户型":titles,"小区地址":position_icons,"建筑信息":house_icons,"单价价格(元/平方)":unit_price,"房子总价/万":total_prices}
info = pd.DataFrame(total)
writer = pd.ExcelWriter("/Users/二手房.xlsx")
info.to_excel(excel_writer = writer,sheet_name = "成都")
writer.save()