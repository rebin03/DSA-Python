def power_set (nums):
    
    result = []
    
    def helper(nums, i, subset):
        if i == len(nums):
            result.append(subset.copy())
            return
            
        # don't add
        helper(nums, i+1, subset)
        # Add
        subset.append(nums[i])
        helper(nums, i+1, subset)
        subset.pop()
    
    helper(nums, 0, [])
    return result


print(power_set([1, 2, 3]))