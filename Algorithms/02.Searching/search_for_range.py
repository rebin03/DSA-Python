def search_for_range(array,target):
    
    left, right = 0, len(array)-1
    first_pos, last_pos = -1, -1
    
    while left <= right:
        
        mid = left + (right-left) // 2
        
        if array[mid] == target:
            if mid == 0 or array[mid-1] != target:
                first_pos = mid
                break
            else:
                right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    left, right = 0, len(array)-1
    
    while left <= right:
        
        mid = left + (right-left) // 2
        
        if array[mid] == target:
            if mid == len(array)-1 or array[mid+1] != target:
                last_pos = mid
                break
            else:
                left = mid + 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return [first_pos, last_pos]


print(search_for_range([1, 1, 2, 2, 2, 3, 4],1))