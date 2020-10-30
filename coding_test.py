def getExchangeName(str):
    exchangeNameList = str.split('_')
    return exchangeNameList[0]

file1 = open('input001.txt', 'r')
Lines = file1.readlines()
# dates set to stores all dates
dates = {}
for i in range(1, len(Lines)):
    tempStr = Lines[i]
    tempList = tempStr.split(',')
    date = int(tempList[0])
    exchange = tempList[1]
    size = int(tempList[4])
    if not date in dates:
        dates[date] = {}
    exchange_name = getExchangeName(exchange)
    date_dic = dates.get(date)
    if not exchange_name in date_dic:
        date_dic[exchange_name] = 0
    date_dic[exchange_name] += size

print("date,exchange,total_bytes")
for date_ in sorted(dates.keys()):
    date_dic_ = dates[date_]
    for exh in sorted(date_dic_.keys()):
        print(str(date_) + "," + exh + "," + str(date_dic_[exh]))











