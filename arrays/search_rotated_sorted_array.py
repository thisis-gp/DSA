# search in rotated sorted array

# linear search
def search_rotated_arr(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print("Index of target: ",search_rotated_arr(nums,target))

# time complexity = O(N)
# space complexity = O(1)

# Optimal solution - binary search - check which half is sorted, elimate the area which does not contain target
def search_rotated_arr(arr,target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # left sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right sorted
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
        


nums = [4,5,6,7,0,1,2]
target = 0
print("Index of target: ",search_rotated_arr(nums,target))

# time complexity = O(logN)
# space complexity = O(1)