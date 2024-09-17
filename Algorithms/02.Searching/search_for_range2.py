def find_left_position(array, target):
    
    left, right = 0, len(array)-1
    
    while left <= right:
        
        mid = left + (right-left) // 2
        
        if array[mid] == target:
            if mid == 0:
                return mid
            elif array[mid-1] == target:
                right = mid - 1
            else:
                return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def find_right_position(array, target):
    
    left, right = 0, len(array)-1
    
    while left <= right:
        
        mid = left + (right-left) // 2
        
        if array[mid] == target:
            if mid == len(array)-1:
                return mid
            elif array[mid+1] == target:
                left = mid + 1
            else:
                return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
    
def search_for_range(array,target):
    
    first_pos = find_left_position(array, target)
    last_pos = find_right_position(array, target)
    return [first_pos, last_pos]

print(search_for_range([1, 1, 2, 2, 2, 3, 4],1))