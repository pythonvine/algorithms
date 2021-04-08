# Binary Search algorithms here 
#Time Complexity:
#The time complexity of Binary Search can be written as

#T(n) = T(n/2) + c '''

def binarySearchAlgo(arr, findingValue, length,left):
    
    while left <= length:
        mid = left + (length - left) // 2

        if arr[mid] == findingValue:
            return mid
        elif arr[mid] < findingValue:
            left = mid + 1
        
        else:
           length = mid -1
    return -1

arr = [1, 2 , 3, 4, 8, 10, 15]

findingValue = 8

results = binarySearchAlgo(arr, findingValue, len(arr)-1, 0)

if results != -1:
    print("Element is present at index %d" %results)
else:
    print("Element is not Present in Array")