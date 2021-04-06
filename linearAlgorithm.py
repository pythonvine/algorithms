
def linearSearchAlgo(arr, findIntergerValue):
    left = 0
    length = len(arr)
    positionPrint = -1
    right = length -1

    for left in range(0, right, 1):
        
        if (arr[left] == findIntergerValue):
            positionPrint = left
            print(f"The Element found in {left} Position {positionPrint + 1} attempt ")
         
            #print("The Element is found at left Position ", left, "with", positionPrint + 1, "Attempt")
            break
        if (arr[right] == findIntergerValue):
            positionPrint = right
            print(f"Element found in Array at position {positionPrint + 1} Position with {length - right} Attampt")
            #print("The Element is found at right Position ", positionPrint + 1, "with", length - right, "Attempt")
            break

        left += 1
        right -= 1
    if positionPrint == -1:
        #print(f"The Element does not found in array {left} Attempt")
        print("The Element is not found in Array with ", left, "Attempt"  )
# Define the variable
arr = [1, 2, 3, 10, 6, 5]
findIntergerValue = 5

linearSearchAlgo(arr, findIntergerValue)