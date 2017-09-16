days = ['월','화','수','목','금','토','일']
date ='2017년4월10일'
month = int(date[date.index('년')+1:date.index('월')])
date = int(date[date.index('월')+1:date.index('일')])-1
day_31 = [1,3,5,7,8,10,12]
totalday = 0
for i in range(1,month):
    if i in day_31:
        totalday += 31
    elif i == 2:
        totalday += 28
    else:
        totalday += 30

totalday += date
print(days[(totalday % 7)])











