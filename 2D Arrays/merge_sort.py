# arr = [12,11,13,5,6,7]

# print("Before Sorting - ",arr)

# def merge(arr, leftArr, rightArr):
#     result = []

#     i = 0
#     j = 0

#     while (i < len(leftArr) and j < len(rightArr)):
#         if leftArr[i] < rightArr[i]:
#             result.append(leftArr[i])
#             i = i+1
#         else:
#             result.append(rightArr[i])
#             j = j+1

#     result.extend(leftArr[i:])
#     result.extend(rightArr[j:])

#     return result

    

# def mergeSort(arr, left, right):
#     if len(arr) == 1:
#         return arr
#     mid = (left + right) // 2

#     leftArr = mergeSort(arr,left,mid)
#     rightArr = mergeSort(arr,mid,right)
#     merge(arr, leftArr, rightArr)



# do a binary search and insert a element

arr = [16]
element = 27
print("Current array: ",arr)


def move_elements(arr, index, element):
    arr.append(element)
    n = len(arr) - 1

    if index != n - 1:
        for i in range(index, n):
            arr[i], arr[n] = arr[n], arr[i]
        
    

def binary_search_insert(arr, element):
    low = 0
    high = len(arr) - 1

    while low<=high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid

        elif arr[mid] > element:
            high = mid - 1

        elif arr[mid] < element:
            low = mid + 1

    return mid

index = binary_search_insert(arr, element)
move_elements(arr,index,element)
print("Array after adding: ",arr)