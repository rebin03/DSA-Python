def selection_sort(nums):
    
    for i in range(len(nums)-1):
        min_index = i
        
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
                
        nums[i], nums[min_index] = nums[min_index], nums[i]
        
    return nums




arr = [4, 8, 2, 6, 1, 5]
print(selection_sort(arr))