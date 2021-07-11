#1Q
import datetime
def convert(date_time):
    format = '%b %d %y %I:%M %p'
    datetime_str = datatime.datatime.strptime(date_time, format)
    return datatime_str
date_time = 'Mar 24 2021 03:24PM'
print(convert(date_time))

#2Q
from datetime import date, timedelta
delta = data.today() - timedelta(5)
print('Current Da datetime import date :',date.today())
print('5 days before Current Date is :',delta)

#3Q
from datetime import datetime
dt = data.today()
print(datetime.combine(dt, datetime.min.time()))

#4Q
import datetime
base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))
