def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = []
n = int(input('Enter length of the array: '))
for k in range(n):
    x = int(input('Enter integer: '))
    arr.append(x)
bubbleSort(arr)
print ("Sorted array is:",  arr)
