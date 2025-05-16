def remove_duplicates(arr, n):
    for i in range(len(arr)-3):
        while arr[i] == arr[i+1]:
            arr.pop(i)
    pass


arr = [0, 1, 1, 1, 2, 3, 4, 4, 5]
n = len(arr)

remove_duplicates(arr, n)
print(arr)
