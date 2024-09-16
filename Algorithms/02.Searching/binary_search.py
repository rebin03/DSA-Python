def binary_search(array,target):
    
    start = 0
    end = len(array) - 1
    
    
    while start <= end:
        
        mid = start + (end-start)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
            
    return -1