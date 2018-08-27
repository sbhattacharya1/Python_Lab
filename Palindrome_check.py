#!/usr/bin/python
# @Program: To Print if a string is palindrome or not
# @Author: Sarani Bhattacharya

x= (str)(input("INPUT : "))

r=''
for i in range(len(x),0,-1):
        r+=x[i-1]

print (r)
if r == x:
        print("%s is a Palindrome" %(x))
else:
        print("%s is not a palindrome" %(x))
