# Bruteforce method

def max_subarryas_sum(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = 0
            for k in range(j+1):
                current_sum += arr[k]
            if current_sum > max_sum :
                max_sum = current_sum

    return max_sum

arr = [2,4,6,8,10]
print("Maximum Sum in Subarrays:",max_subarryas_sum(arr))

# time complexity: O(N^3)
# space complexity: O(1)
# total subarrays: n(n-)/2

# Improved Solution - prefix array
def max_subarryas_sum(arr):
    max_sum = float("-inf")
    prefix_arr = [0] * len(arr)
    prefix_arr[0] = arr[0]
    for index in range(1,len(arr)):
        prefix_arr[index] = prefix_arr[index-1] + arr[index]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = prefix_arr[j] if i == 0 else prefix_arr[j] - prefix_arr[i-1]
            if current_sum > max_sum:
                max_sum = current_sum
            

    return max_sum

arr = [2,4,6,8,10]
print("Maximum Sum in Subarrays:",max_subarryas_sum(arr))

# time complexity: O(N^2)
# space complexity: O(N)
# total subarrays: n(n-)/2

# Optimized Solution - Kadane 's Algorithm
def max_subarryas_sum(arr):
    max_sum = float("-inf")
    current_sum = 0
    for index in range(len(arr)):
        current_sum += arr[index]
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum 

    all_negative = True
    smallest_neg_value = float("-inf")
    for ele in arr:
        if ele > 0:
            all_negative = False
        if ele > smallest_neg_value:
            smallest_neg_value = ele

    if all_negative:
        return smallest_neg_value                        
    return max_sum

arr = [2,4,6,8,10]
print("Maximum Sum in Subarrays:",max_subarryas_sum(arr))

# time complexity: O(N)
# space complexity: O(1)
# total subarrays: n(n-)/2

# edge case - kadane 's algorithm will not work for all negative 
# numbers list it will return 0 only
