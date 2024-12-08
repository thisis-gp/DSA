def bin_search(arr, key, start, end):
    if end>=start:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return bin_search(arr, key, start, mid-1)
        else:
            return bin_search(arr,key,mid+1, end)
    else:
        return -1

arr = [10,20,30,40,50]
key = 50
result = bin_search(arr,key,0,len(arr)-1)

if result!=-1:
    print(result)
else:
    print("Not found")
