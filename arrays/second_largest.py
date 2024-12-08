# Brute Force method
def second_largest(arr):
    arr.sort(reverse=True)
    max_ele = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < max_ele :
            return arr[i]
    return -1


arr = [12,35,1,10,34,1]
print("Second largest is ",second_largest(arr))

# time complexity: O(NlogN + N)
# space complexity: O(1)


# Two iterations
def second_largest(arr):
    max_ele = 0
    second_max_ele = 0
    for i in arr:
        if i > max_ele:
            max_ele = i
    
    for i in arr:
        if i > second_max_ele and i < max_ele:
            second_max_ele = i
    
    return second_max_ele

arr = [12,35,1,10,34,1]
print("Second largest is ",second_largest(arr))

# time complexity: O(2N)
# space complexity: O(1)

# optimal solution: one iteration

def second_largest(arr):
    n = len(arr)
    if n<2:
        return -1
    
    max_ele = float("-inf")
    second_max_ele = float("-inf")
    
    for i in arr:
        if i > max_ele:
            second_max_ele = max_ele
            max_ele = i
        elif i>second_max_ele and i<max_ele:
            second_max_ele = i
    
    if second_max_ele == float("-inf"):
        return -1
    else:
        return second_max_ele

arr = [12,35,1,10,34,1]
print("Second largest is ",second_largest(arr))

# time complexity: O(2N)
# space complexity: O(1)