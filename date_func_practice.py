#!/usr/bin/python
# @Program: To Practice different functionalities of Date function
# @Author: Sarani Bhattacharya

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
# print today's date
print ("today is: " + str(datetime.now()))

# print today's date one year from now
print ("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))

#Using today() function from date class
print(date.today())

day=(str)(date.today().day)
mon=(str)(date.today().month)
yr=(str)(date.today().year)

print("Today :\nDay:" + day +"\nMonth:" + mon +"\nYear:" + yr)

wkday=(str)(date.today().weekday())

#Print Day of week where index starts from 0, for Monday
print("Day of Week:" + wkday)
