# Diagonal Sum

# Brute Force Approach
def diagonal_sum(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                sum += arr[i][j]
            else:
                if i + j == len(arr) - 1:
                    sum += arr[i][j]

    return sum
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimized Approach

def diagonal_sum(arr):
    sum = 0
    for i in range(len(arr)):
        # primary diagonal
        sum += arr[i][i]
        # secondary diagonal
        if (i != len(arr) - i - 1):
            sum += arr[i][len(arr) - i - 1]

    return sum

# Time Complexity = O(n)
# Space Complexity = O(1)

arr = [[1,2,3,4],[5,6,7, 8],[9,10,11,12],[13,14,15,16]]
print(diagonal_sum(arr))