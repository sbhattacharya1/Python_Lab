#!/usr/bin/python
# @Program: To understand the use of tuples, lists, dictionary
# @Author: Sarani Bhattacharya

#Python Lists
list1=['abcd',789,2.23,'John',70.2]
tinylist=[123,'James']
print (list1[0])					        #1st element of list1
print (list1[1:3])					      #789 and 2.23 , From 1st to 2nd (less than 3rd index)
print (list1*2)						        #Print list1 twice
print (list1 + tinylist)			    #Concatenate 2 lists
list1[3]='Jinny'					        #Modify element in 3rd index
print (list1)

#Sample Built-in list Functions
list1.append(4587)					      #Append 4587 at the end
print (list1)
num=[3,7,2,9,1]
sorted_num=sorted(num,reverse=True)   #list "num" will be sorted in descending order and stored in new list "sorted_num"
num.sort()                        #num will be sorted and replaced
num.reverse()                     #reverse the order of elelemnts in num
del num[1]                        #element in 1st index will be deleted
a=num.pop(1)                      #element in 1st position will be removed and returned in a
list1.remove('John')              #remove element wise  
c=num.count(1)                    #count and return the number of occurance of element "1"
i=num.index(1)                    #return the index of 1st occurance of element "1"

#Python Tuples						        Tuples are read-only
t1=('abcd',789,2.23,'john',70.2)

