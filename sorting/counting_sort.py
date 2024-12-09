# Counting Sort

def counting_sort(arr):
    largest = float("-inf")
    for i in range(len(arr)):
        largest = max(arr[i],largest)

    count = [0] * (largest + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1

    # sorting
    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1
    
arr = [5,4,1,3,2]
counting_sort(arr)
print(arr)
    
# time complexity = O(2N + range)

# edge case - have to treat negative numbers by converting them to postive then showing them in descending order

def desc_counting_sort(arr):
    largest = float("-inf")
    for i in range(len(arr)):
        largest = max(largest, arr[i])

    count = [0] * (largest + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1

    j = 0
    for i in range(len(count)-1,0,-1):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

arr = [3,6,2,1,8,7,4,5,3,1]
desc_counting_sort(arr)
print(arr)