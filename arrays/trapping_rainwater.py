# Trapping rainwater - we need to fing how much water can be trapped between
# water level = min(max_left, max_right)
# trapped_water = (water_level - height) * width
# We will use Auxilary arrays to store left max boundary and right max boundary

def trapped_rainwater(arr):
    n = len(arr)

    left_max_boundary = [0] * n
    right_max_boundary = [0] * n

    # calculate left max boundary
    left_max_boundary[0] = arr[0]
    for i in range(1,n):
        left_max_boundary[i] = max(arr[i], left_max_boundary[i-1])

    # calculate right max boundary
    right_max_boundary[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right_max_boundary[i] = max(arr[i], right_max_boundary[i+1])
    
    # calculate water level
    trapped_water = 0
    for i in range(n):
        water_level = min(left_max_boundary[i],right_max_boundary[i])
        trapped_water += water_level - arr[i]

    return trapped_water

height = [4,2,0,6,3,2,5]
print("Trapped rainwater is",trapped_rainwater(height))

# time complexity = O(N)
# space complexity = O(N)