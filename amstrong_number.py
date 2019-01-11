#!/usr/bin/python
# @Program: To Print if a number is Amstrong or not
# A sample amstrong number : 153= 1^3 + 5^3 + 3^3 = 153 (no of digits in 153=3)
# @Author: Sarani Bhattacharya

print("****Program To check Amstrong Number****")
num=input("Please provide a number: ")

digits=len(num)                       #get the number of digits in the number
num=int(num)
temp_num=num
ams=0
for i in range(0,digits):
    tup=divmod(temp_num,10)           #tuple tup to store quotient and remainder
    temp_num=tup[0]
    ams+=tup[1]**digits
    
if ams == num : 
    print("{} is an Amstrong number".format(num))
else:
    print("{} is not an Amstrong number".format(num))
