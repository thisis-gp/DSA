# Subarrays: contingous part of arrays

def subarryas(arr):
    subarryas_lst = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            subarryas_lst.append(arr[i:j])

    return subarryas_lst

arr = [2,4,6,8,10]
print("Subarrays:",subarryas(arr))

# time complexity: O(N^2)
# space complexity: O(N)
# total subarrays: n(n-)/2

