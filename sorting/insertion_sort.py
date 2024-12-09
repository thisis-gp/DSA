# insertion_sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i - 1
        while prev>=0 and arr[prev] > curr:
            arr[prev+1] = arr[prev]
            prev -= 1
        arr[prev+1] = curr
        

arr = [5,4,1,3,2]
insertion_sort(arr)
print(arr)

# time complexity = O(N^2)
# space complexity = O(1)

# descending order

def desc_insertion_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] < curr:
            arr[prev+1] = arr[prev]
            prev -= 1
        
        arr[prev + 1] = curr

arr = [3,6,2,1,8,7,4,5,3,1]
desc_insertion_sort(arr)
print(arr)
