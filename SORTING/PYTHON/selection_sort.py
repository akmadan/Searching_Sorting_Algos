def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = []
n = int(input('Enter no. of integers: '))
for i in range(n):
    x = int(input('Enter integer: '))
    arr.append(x)
arr = selection_sort(arr)
print ("Sorted array: ", arr)
