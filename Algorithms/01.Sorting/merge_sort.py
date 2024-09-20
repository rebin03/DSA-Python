def merge_sort(array):
    
    if len(array) <= 1:
        return array
        
    mid = len(array)//2
    
    left_half = array[:mid]
    right_half = array[mid:]
    
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    return merge(sorted_left, sorted_right)
    
def merge(left, right):
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(merge_sort(arr))