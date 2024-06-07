import requests
from bs4 import BeautifulSoup
import jieba
from pyecharts.charts import WordCloud

url = "https://nocturne-spider.baicizhan.com/practise/29.xml"
response = requests.get(url)
response.encoding = response.apparent_encoding
xml = response.text
soup = BeautifulSoup(xml, "lxml")
content_all = soup.find_all(name="d")
wordList = []

for comment in content_all:
    data = comment.string
    words = jieba.lcut(data)
    wordList = wordList + words
wordDict = {}
for word in wordList:
    if len(word) > 1:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict[word] + 1
wordCloud = WordCloud()
wordCloud.add(series_name='', data_pair=wordDict.items(), word_size_range=[20, 80])
wordCloud.render('wordcloud.html')
print('success')