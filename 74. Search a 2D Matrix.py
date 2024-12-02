matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 30

def searchMatrix(matrix, target):
    # set to final line (target higher than first number in last line)
    searchIndex = len(matrix) - 1

    for i in range(len(matrix)):
        if target == matrix[i][0]:
            return True
        
        elif target < matrix[i][0]:
            searchIndex = i - 1
            break

    
    if target in matrix[searchIndex]:
        return True
    
    else:
        return False

print(searchMatrix(matrix, target))