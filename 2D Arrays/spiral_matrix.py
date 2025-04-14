# spiral matrix

def spiral_matrix(arr):
    start_row = 0
    start_col = 0

    end_row = len(arr) - 1
    end_col = len(arr[0]) - 1

    if end_col == 0:
        for i in range(start_row, end_row + 1):
            print(arr[i][start_col])

    else:
        
        while (start_row <= end_row and start_col <= end_col):
            # top
            for i in range(start_col, end_col + 1):
                print(arr[start_row][i])

            # right
            for i in range(start_row + 1, end_row + 1):
                print(arr[i][end_col])
            
            # bottom
            if start_row < end_row:
                for i in range(end_col - 1, start_col - 1, -1):
                    print(arr[end_row][i])
            
            # left
            if start_col < end_col:
                for i in range(end_row - 1, start_row, -1):
                    print(arr[i][start_col])
            
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1

arr = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]

spiral_matrix(arr)


    