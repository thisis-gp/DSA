# brute force

def rotate_arr(arr,d):
    d = d % len(arr)

    temp = arr[:d]

    for i in range(d,len(arr)):
        arr[i-d] = arr[i]

    J = 0
    for i in range(len(arr) - d,len(arr)):
        arr[i] = temp[J]
        J += 1

arr = [1,2,3,4,5,6,7]
k = 3

rotate_arr(arr,k)
print(arr)

# better approach

def rotate_arr(arr,d):
    d = d % len(arr)

    temp = arr[:d]

    for i in range(d,len(arr)):
        arr[i-d] = arr[i]

    for i in range(len(arr) - d,len(arr)):
        arr[i] = temp[i - (len(arr) - d)]

arr = [1,2,3,4,5,6,7]
k = 3

rotate_arr(arr,k)
print(arr)

# Time complexity : O(D) + O(N-D) + O(D) = O(N+D)
# Space Complexity : O(D)

# optimal solution

def rotate_arr(arr,d):
    d = d % len(arr)

    l,r = 0,d - 1
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l,r = l+1, r-1
    
    l,r = d,len(arr)-1
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l,r = l+1, r-1

    l,r = 0,len(arr) - 1
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l,r = l+1, r-1
    

arr = [1,2,3,4,5,6,7]
k = 3

rotate_arr(arr,k)
print(arr)

# Time complexity : O(D) + O(N-D) + O(N) = O(2N)
# Space Complexity : O(1)