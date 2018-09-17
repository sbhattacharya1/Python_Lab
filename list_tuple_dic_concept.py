#!/usr/bin/python
# @Program: To understand the use of tuples, lists, dictionary
# @Author: Sarani Bhattacharya

#Python Lists
list1=['abcd',789,2.23,'John',70.2]
tinylist=[123,'James']
print (list1[0])					#1st element of list1
print (list1[1:3])					#789 and 2.23 , From 1st to 2nd (less than 3rd index)
print (list1*2)						#Print list1 twice
print (list1 + tinylist)			#Concatenate 2 lists
list1[3]='Jinny'					#Modify element in 3rd index
print (list1)

#Built in list Functions
list1.append(4587)					#Append 4587 at the end
print (list1)

#Python Tuples						Tuples are read-only
tuple1=('abcd',789,2.23,'john',70.2)
