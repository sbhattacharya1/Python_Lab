#!/usr/bin/python
# @Program: To Print Fibonacci series upto N number
# @Author: Sarani Bhattacharya
from sys import argv

def  fibonacci_series(n):
    x,y=0,1
    print ("Fibonacci Series(%d):" %(n))
    print (" %d " %(x), end =' ')
    for i in range(1,n):
            print (" %d " %(y), end =' ')
            z=x+y
            x=y
            y=z
    return;

#Main 
if len(argv) !=2:
    exit(1)
n=int(argv[1])
fibonacci_series(n)
