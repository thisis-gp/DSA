rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

arr = [[0 for i in range(rows)] for j in range(columns)]

print("Enter elements: ")
for i in range(rows):
    for j in range(columns):
        ele = int(input())
        arr[i][j] = ele

print(arr)

def search_element(arr, key):
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == key:
                print("Element found at",[i,j])

def greatest_smallest_element(arr):
    greatest = float("-inf")
    smallest = float("inf")
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] > greatest:
                greatest = arr[i][j]
            if arr[i][j] < smallest:
                smallest = arr[i][j]
    print("Greatest is", greatest)
    print("Smallest is ", smallest)

search_element(arr, 5)
greatest_smallest_element(arr)