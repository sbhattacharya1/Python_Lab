import numpy as np

#Binary Search 
def binary_search(array,low,high,item):
    while(low<=high):
        mid=(high+low)//2
        if(item == array[mid]):           
            print("Element found in position {}".format(mid))
            return 
        else:
            if(item>array[mid]):               
                low=mid+1
            else:               
                high=mid-1
        
    print("Element Not Found")  
    return


#binary search with recursion
def binary_search_rec(array,low,high,item):

        mid=(high+low)//2
        
        if(item == array[mid]):           
            return mid
        elif(low<=high):
            if(item>array[mid]):               
                return binary_search_rec(array,mid+1,high,item)
            else:               
                return binary_search_rec(array,low,mid-1,item)
        else:
            return -1
    
    


arr = np.array([],dtype=int)
n=int(input("Please Enter number of elements in the array:"))
print("Please Enter the elements : ")
for i in range(n):
    x=int(input())
    arr=np.append(arr,x)


arr.sort()
print("The sorted array is : ", arr)
item=int(input("Please enter the element to search: "))
binary_search(arr,0,n-1,item)

print("Same Searching with Recursive function call")

pos=binary_search_rec(arr,0,n-1,item)
print(pos)
if(pos == -1):
    print("Element Not Found")
else:
    print("Element Found in position : {}".format(pos))