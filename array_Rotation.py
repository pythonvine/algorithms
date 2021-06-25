# Condition
# 1<N<100
# 1<D<N-1

def arrRotation(arr, d, n):
    for i in range(d):
        temp= arr[0]
        for i in range(n-1):

        # print(temp)
            arr[i] = arr[i+1]
        # print(arr)
        arr[-1] = temp
        # print(arr)
    print(arr)
        
   # print(arr)


print('Input: ')    
n = 77
arr = [40, 13, 27, 87, 95, 40, 96, 71, 35, 79, 68, 2, 98, 3, 18, 93, 53, 57, 2, 81, 87, 42, 66, 90, 45, 20, 41, 30, 32, 18, 98, 72, 82, 76, 10, 28, 68, 57, 98, 54, 87, 66, 7, 84, 20, 25, 29, 72, 33, 30, 4, 20, 71, 69, 9, 16, 41, 50, 97, 24, 19, 46, 47, 52, 22, 56, 80, 89, 65, 29, 42, 51, 94, 1, 35, 65, 25]
print(arr)
d = 69
print('Output:')
arrRotation(arr, d, n)