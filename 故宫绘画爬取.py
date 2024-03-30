import requests
from bs4 import BeautifulSoup
import re
import os

def clean_filename(filename):
    """清理文件名中的非法字符"""
    filename = re.sub(r'[\\/*?:"<>|]', '', filename)
    filename = filename.replace('\t', '').replace('\n', '')  # 移除制表符和换行符
    filename = filename.strip()
    return filename

def make_safe_directory(path):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(path):
        os.makedirs(path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
base_url = 'https://www.dpm.org.cn'
start_page = '/lights/royal.html'

# 设定一个目录来保存所有图片
images_directory = 'downloaded_images'
make_safe_directory(images_directory)

def download_image(img_url, img_name):
    """下载并保存图片"""
    img_response = requests.get(img_url, headers=headers)
    img = img_response.content
    img_path = os.path.join(images_directory, f'{img_name}.jpg')
    with open(img_path, 'wb') as f:
        f.write(img)
    print(f"Image saved: {img_path}")

def process_page(url):
    """处理单个页面的图片下载"""
    response = requests.get(url, headers=headers)
    html = response.content.decode(response.apparent_encoding)
    soup = BeautifulSoup(html, 'lxml')
    content_all = soup.find_all(class_='pic')
    for content in content_all:
        img_content = content.find(name='img')
        img_url = img_content.attrs['src']
        if not img_url.startswith('http'):
            img_url = base_url + img_url  # 处理相对URL
        img_name = clean_filename(img_content.attrs['alt'])  # 清理文件名
        download_image(img_url, img_name)

# 处理初始页面
process_page(base_url + start_page)

# 处理其他页面
for i in range(2, 142):
    next_page = f'/lights/royal/p/{i}.html'
    process_page(base_url + next_page)
