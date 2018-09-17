#!/usr/bin/python
# @Program: To Find if a year is leap year or not
# @Author: Sarani Bhattacharya

year=(int)(input("Tell me a year"));

if year % 100 == 0 :
	if year % 400 == 0 :
		print("%d is a leap Year" %(year));
	else:
		print("%d is not a leap Year" %(year));
else:
	if year % 4 == 0:
		print("%d is a leap Year" %(year));
	else:
		print("%d is not a leap Year" %(year));
