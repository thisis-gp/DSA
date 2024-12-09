# selection sort

def selection_sort(arr):
    for i in range(len(arr)-1):
        minPos = i
        for j in range(i+1, len(arr)):
            if arr[minPos] > arr[j]:
                minPos = j

        arr[i],arr[minPos]=arr[minPos],arr[i]

arr = [5,4,1,3,2]
selection_sort(arr)
print(arr)

# time complexity = O(N^2)
# space complexity = O(1)

# descending order


def desc_selection_sort(arr):
    for i in range(len(arr)-1):
        minPos = i
        for j in range(i+1, len(arr)):
            if arr[minPos] < arr[j]:
                minPos = j

        arr[i],arr[minPos]=arr[minPos],arr[i]

arr = [3,6,2,1,8,7,4,5,3,1]
desc_selection_sort(arr)
print(arr)