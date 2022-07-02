import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '季度数据.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    print(header_row)
#    for index,column_header in enumerate(header_row):
#        print(index,column_header)

file2 = 'data/sitka_weather_2018_simple.csv'
with open(file2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    for index, column_header in enumerate(header_row):
#        print(index,column_header)

    #从文件中获取最高温度
    dates,highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

#根据最高气温绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red')

#设置图形的格式
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()