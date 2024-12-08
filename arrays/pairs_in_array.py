def pairs_in_array(arr):
    pairs_lst = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            pairs_lst.append((arr[i],arr[j]))

    return pairs_lst

arr = [2,4,6,8,10]
print("Pairs in array:",pairs_in_array(arr))

# time complexity: O(N^2)
# space complexity: O(N)
# total number of pairs : n(n-1)/2 