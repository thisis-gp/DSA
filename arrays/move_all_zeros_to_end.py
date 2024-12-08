# Brute force method
def move_zero_to_end(arr):
    temp_arr = []
    for i in arr:
        if i != 0:
            temp_arr.append(i)
    
    if temp_arr:
        n = len(temp_arr)
        for i in range(len(temp_arr)):
            arr[i] = temp_arr[i]

        for i in range(n, len(arr)):
            arr[i] = 0
    return arr

arr = [0,5,0,3,4,0,2,1]
print("Array is ",move_zero_to_end(arr))

# time complexity : O(N) + O(X) + O(N-X) = O(N)
# Space complexity : O(N)

# Optimal solution - two pointer
def move_zero_to_end(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    
    if j!= -1:
        for i in range(j+1,len(arr)):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                j += 1

arr = [0,5,0,3,4,0,2,1]
move_zero_to_end(arr)
print("Array is ",arr)

# Time complexity : O(X) + O(N-X) = O(N)
# Space complexity : O(1)
