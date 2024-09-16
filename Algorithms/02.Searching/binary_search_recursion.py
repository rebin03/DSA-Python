def binay_search(nums, target):
    
    def helper(nums, target, left, right):
        if left > right: return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return helper(nums, target, mid + 1, right)
        else:
            return helper(nums, target, left, mid - 1)
    
    return helper(nums, target, 0, len(nums)-1)


print(binay_search([1, 2, 3, 5, 6, 7, 8, 9, 12, 15, 19, 22, 25], 9))