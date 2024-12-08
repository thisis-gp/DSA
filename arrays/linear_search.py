def linear_search(arr,element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

index = linear_search([1,2,3,4,5,6],5)
if index != -1 :
    print("Element found at ",index)
else:
    print("Element not found")