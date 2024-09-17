def find_left_position(array, target, range, left, right):
    
    if left > right: return
    
    mid = left + (right-left) // 2
    
    if array[mid] == target:
        if mid == 0 or array[mid-1] != target:
            range[0] = mid
        else:
            find_left_position(array, target, range, left, mid-1)
            
    elif array[mid] < target:
        find_left_position(array, target, range, mid+1, right)
    else:
        find_left_position(array, target, range, left, mid-1)
        

def find_right_position(array, target, range, left, right):
    
    if left > right: return
    
    mid = left + (right-left) // 2
    
    if array[mid] == target:
        if mid == len(array)-1 or array[mid+1] != target:
            range[1] = mid
        else:
            find_right_position(array, target, range, mid+1, right)
            
    elif array[mid] < target:
        find_right_position(array, target, range, mid+1, right)
    else:
        find_right_position(array, target, range, left, mid-1)
        
    
def search_for_range(array,target):
    range = [-1, -1]
    find_left_position(array, target, range, 0, len(array)-1)
    find_right_position(array, target, range, 0, len(array)-1)
    return range

print(search_for_range([1, 1, 2, 2, 2, 3, 4],1))