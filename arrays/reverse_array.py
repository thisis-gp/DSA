def rev_arr(arr):
    end = len(arr) -1
    start = 0
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [2,4,6,8,10]
print("Before: ",arr)
print("After: ", rev_arr(arr))

# time complexity = O(N)
# space complexity = O(n)
