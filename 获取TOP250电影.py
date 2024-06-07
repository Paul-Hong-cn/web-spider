# 使用import导入requests模块
import requests

# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
# TODO 使用for循环遍历range()函数生成的0-9的数字
for i in range(0,10):

    # TODO 取遍历中的每个数和25相乘计算每页的数值，并赋值给page
    page = i * 25

    # TODO 用"https://movie.douban.com/top250?start="和page转换成的字符串格式相连，接着连上"&filter="，并赋值给url
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='

    # TODO 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
    response = requests.get(url,headers = headers)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,'lxml')

    # TODO 使用find_all()查询soup中class="pic"的节点，赋值给content_all
    content_all = soup.find_all(class_ = 'pic')

    # TODO for循环遍历content_all
    for content in content_all:

        # TODO 使用find()查询content中的img标签，并赋值给imgContent
        imgContent = content.find(name = 'img')

        # TODO 使用.attrs获取imgContent的alt的属性值，并赋值给imgName
        imgName = imgContent.attrs['alt']

        # TODO 使用.attrs获取imgContent的src的属性值，并赋值给imgUrl
        imgUrl = imgContent.attrs['src']

        # TODO 使用replace()函数将链接中的s_ratio_poster替换成m，并赋值给imgUrlHd
        imgUrlHd = imgUrl.replace('s_ratio_poster','m')

        # TODO 将链接添加进requests.get()中，赋值给imgResponse
        imgResponse = requests.get(imgUrlHd)

        # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
        img = imgResponse.content

        # TODO 使用with语句配合open()函数以图片写入的方式打开文件
        # 用格式化将图片名字和.jpg格式组合
        # 打开的文件赋值为f
        with open(f'{imgName}.jpg','wb') as f:
            # TODO 使用write()将图片写入
            f.write(img)
        print(f"downloaded:{imgName}")