def search_in_matrix(matrix,target):
    
    if len(matrix) == 0:
        return False

    top, bottom = 0, len(matrix)-1
    no_col = len(matrix[0])-1
    
    while top <= bottom:
        
        mid = (top + bottom) // 2
        
        if target < matrix[mid][0]:
            bottom = mid - 1
        elif target > matrix[mid][no_col]:
            top = mid + 1
        else:
            break
        
    if top > bottom: return False
    
    left, right = 0, no_col
    
    while left <= right:
        mid2 = (left + right) // 2
        
        if matrix[mid][mid2] == target:
            return True
        elif matrix[mid][mid2] > target:
            right = mid2 - 1
        else:
            left = mid2 + 1
    return False

print(search_in_matrix([[1,2,3],[4,5,6],[9,10,11]], 10))