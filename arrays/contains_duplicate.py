def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
nums = [1,2,3,1]
print("Contains duplicate:",contains_duplicate(nums))

# time complexity : O(N^2)
# space complexity : O(1)

# improves solution - sorting the array, same numbers come adjacent
def contains_duplicate(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False

nums = [1,2,3,1]
print("Contains duplicate:",contains_duplicate(nums))

# time complexity : O(NlogN)
# space complexity : O(1)

# optimal solution - hash map
# storing the values in a dictionary and checking
def contains_duplicate(arr):
    hash_set = set()
    for i in arr:
        if i in hash_set:
            return True
        hash_set.add(i)
    return False

nums = [1,2,3,1]
print("Contains duplicate:",contains_duplicate(nums))

# time complexity : O(N)
# space complexity : O(N)