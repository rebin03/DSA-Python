def monotonic_array(array):
    
    is_increasing = False
    is_decreasing = False
        
    for i in range(len(array)-1):
        
        if array[i] >= array[i+1]:
            is_increasing = True
        else:
            is_decreasing = True
            
        if is_increasing and is_decreasing:
            return False
        
        
    return True