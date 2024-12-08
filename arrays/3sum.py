# brute force method

def three_sum(arr):
    hash_set = set()
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    lst = [arr[i],arr[j],arr[k]]
                    lst.sort()
                    hash_set.add(tuple(lst))
    return [list(triplet) for triplet in hash_set]

nums = [-1,0,1,2,-1,-4]
print("Pairs are ",three_sum(nums))

# time complexity: O(N^3) + O(NlogN)
# space complexity: O(N)

# hashing - avoids 3 rd loop

def three_sum(arr):
    triples = set()
    for i in range(len(arr)-2):
        hash_set = set()
        for j in range(i+1,len(arr)-1):
            third = - (arr[i] + arr[j])
            if third in hash_set:
                lst = [arr[i],arr[j],third]
                lst.sort()
                triples.add(tuple(lst))
            hash_set.add(arr[j])
            
    return [list(triplet) for triplet in triples]

nums = [-1,0,1,2,-1,-4]
print("Pairs are ",three_sum(nums))

# time complexity: O(N^2 log N)
# space complexity: O(N)

# optimal solution - two pointer approach

def three_sum(arr):
    arr.sort()
    triples = list()

    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
        j =i+1
        k = len(arr) - 1
        while j<k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                lst = [arr[i], arr[j], arr[k]]
                triples.append(lst)
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
    return triples


nums = [-1,0,1,2,-1,-4]
print("Pairs are ",three_sum(nums))

# time complexity: O(NlogN + N^2)
# space complexity: O(N)