import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line

url = "https://nocturne-spider.baicizhan.com/practise/34.xml"
response = requests.get(url)
response.encoding = response.apparent_encoding
xml = response.text
soup = BeautifulSoup(xml, "lxml")
content_all = soup.find_all(name="d")

timeList = []
for content in content_all:
    data = content.attrs['p']
    time = data.split(',')[0]
    timeList.append(float(time))

subtitlesDict = {}
for x in range(13):
    start = 60 * x + 1
    end = 60 * (x + 1)
    segment_range = f"{start}-{end}"
    subtitlesDict[segment_range] = 0

for subtitle in subtitlesDict.keys():
    start_key = subtitle.split('-')[0]
    end_key = subtitle.split('-')[1]
    for time in timeList:
        if int(start_key) <= time < int(end_key):
            subtitlesDict[subtitle] = subtitlesDict[subtitle] + 1

line = Line()
line.add_xaxis(list(subtitlesDict.keys()))
line.add_yaxis('弹幕数',list(subtitlesDict.values()))
line.render('line.html')
print('success')