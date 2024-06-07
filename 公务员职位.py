# 导入requests模块
import requests
# 导入bs4中的BeautifulSoup模块
from bs4 import BeautifulSoup
# 导入pandas模块并以pd调用
import pandas as pd

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

#  新建用于存储地区、部门、用人司局、职位名称的列表
areaList = []
departmentList = []
companyList = []
positionList = []

# 使用for循环和range()生成1-5的变量并遍历
for page in range(1, 6):

    # 使用格式化组合链接
    url = f"https://nocturne-spider.baicizhan.com/practise/60/PAGE/{page}.html"
    # 使用get()函数请求链接，并且带上headers
    response = requests.get(url, headers=headers)
    # 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
    html = response.text
    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 是时候爬取网页表格数据了
    table = soup.find(class_='table fsk01')
    content_all = table.find_all('tr')[1:]
    for content in content_all:
        contents = content.find_all('td')
        contentList = contents[:4]
        area = contentList[0].string
        areaList.append(area)
        department = contentList[1].string
        departmentList.append(department)
        company = contentList[2].string
        companyList.append(company)
        position = contentList[3].string
        positionList.append(position)
total = {"地区": areaList, "部门": departmentList, "用人司局": companyList, "职位名称": positionList}
info = pd.DataFrame(total)
writer = pd.ExcelWriter("公务员职位信息.xlsx")
info.to_excel(excel_writer=writer, sheet_name="计算机科学与技术")
writer._save()