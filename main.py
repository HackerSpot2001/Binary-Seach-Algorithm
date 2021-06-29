#!/usr/bin/python3

def binarySearchAppr (arr, start, end, x):
    if end >= start:
        mid = start + (end- start)//2
    # If element is present at the middle
        if arr[mid] == x:
            return mid
    # If element is smaller than mid
        elif arr[mid] > x:
            return binarySearchAppr(arr, start, mid-1, x)
        # Else the element greator than mid
        else:
            return binarySearchAppr(arr, mid+1, end, x)
    else:
        return -1
   # Element is not found in the array
arr = sorted(['t','u','t','o','r','i','a','l'])
x ='o'
result = binarySearchAppr(arr, 0, len(arr)-1, x)
if result != -1:
   print ("Element is present at index "+str(result))
else:
    print ("Element is not present in array")