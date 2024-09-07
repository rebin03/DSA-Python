def max_area(array):
    max_area = 0

    left, right = 0, len(array)-1
    
    while left < right:
        
        width = right-left
        current_area = min(array[left], array[right]) * width
        
        if current_area > max_area:
            max_area = current_area
            
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(max_area([3,7,5,6,8,4]))