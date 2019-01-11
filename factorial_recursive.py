#!/usr/bin/python
# @Program: To Print Factorial of a number N, function in recursive nature
# @Author: Sarani Bhattacharya

#Recursive function for factorial
def fact(n):
    if n<=1:
        return 1 
    else: 
        return n*fact(n-1)


num=int(input("Please enter a number: "))                           #Get the number
print("Factorial of {} is :{}".format(num,fact(num)))               #Print the factorial
