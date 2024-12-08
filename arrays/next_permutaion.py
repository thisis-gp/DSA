def nextPermutation(arr):
    ind = -1
    n = len(arr) - 1
    for i in range(n - 1, -1, -1):
        if arr[i] < arr[i+1]:
            ind = i
            break
    
    if ind == -1:
        arr.reverse()

    for i in range(n, ind, -1):
        if arr[i] > arr[ind]:
            arr[i] , arr[ind] = arr[ind], arr[i]
            break

    arr[ind+1:] = reversed(arr[ind+1:])

arr = [1, 2, 3, 6, 5, 4]
nextPermutation(arr)
print("Next permutation: ",arr)