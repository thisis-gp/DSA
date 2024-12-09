def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 

arr = [55,4,1,31,-2]
bubble_sort(arr)
print(arr)

# time complexity = O(N^2)
# space complexity = O(1)

# the problem is if the array is already sorted then also it will take O(N^2) time

# optimal solution
def op_bubble_sort(arr):
    for i in range(len(arr) - 1):
        swaps = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                swaps += 1
        if swaps == 0: # already sorted
            break 

arr = [1,2,3,4,5]
op_bubble_sort(arr)
print(arr)

# time complexity = O(N^2)
# space complexity = O(1)

# descending order

def descending_bubble_sort(arr):
    for i in range(len(arr) - 1):
        swaps = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                swaps += 1
        if swaps == 0: # already sorted
            break 

arr = [3,6,2,1,8,7,4,5,3,1]
descending_bubble_sort(arr)
print(arr)