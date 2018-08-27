#!/usr/bin/python
# @Program: To Print Fibonacii series upto N number
# @Author: Sarani Bhattacharya
from sys import argv

def  fibonacii_series(n):
    x,y=0,1
    print ("Fibonacii Series(%d):" %(n))
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
fibonacii_series(n)
