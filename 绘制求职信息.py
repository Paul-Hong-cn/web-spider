from pyecharts.charts import Bar
with open(r"D:\Python-3.12\VSCode\夜曲编程\职位数据.txt", "r",encoding = 'utf-8') as f:
    dataList = f.readlines()

cityDict = {}
for data in dataList:
    if '薪资面议' in data:
        continue
    city = data.split(',')[2]
    salary = data.split(',')[3]
    daily = salary.split('/')[0]
    if '-' in daily:
        start = daily.split('-')[0]
        end = daily.split('-')[1]
        average = (int(start) + int(end)) / 2
    elif daily.isdigit():
        average = float(daily)
    else:
        continue
    if city not in cityDict.keys():
        cityDict[city] = []
    cityDict[city].append(average)

city_num_dict = {}
for key, value in cityDict.items():
    average_value = sum(value) // len(value)
    cityDict[key] = average_value
    city_num_dict[key] = len(value)

bar = Bar()
bar.add_xaxis(list(cityDict.keys()))
bar.add_yaxis('工资平均值', list(cityDict.values()))
bar.render('salary.html')
bar_city = Bar()

bar_city.add_xaxis(list(city_num_dict.keys()))
bar_city.add_yaxis('职位数量', list(city_num_dict.values()))
bar_city.render('positions.html')