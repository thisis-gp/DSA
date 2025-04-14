# Search in Sorted Matrix

# Bruteforce Approach
# Time Complexity - O(n^2)

# Row Wise Binary Search
# Time Complexity - O(nlogn)

# Staircase Search
# Time Complexity - O(n)

def staircase_search(matrix, key):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == key:
            print(f"Element {key} found at ({row}, {col})")
            return True
        elif matrix[row][col] > key:
            col -= 1
        else:
            row += 1
    print(f"Element {key} not found")
    return False
            
matrix = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
key = 33
print(staircase_search(matrix, key))
