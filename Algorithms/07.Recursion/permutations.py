def all_permutations(nums):
    
    lst = []
    
    if len(nums) == 0: return [[]]
    
    def helper(nums, i):
        
        if i == len(nums)-1:
            lst.append(nums.copy())
        
        for j in range(i, len(nums)):
            
            nums[i], nums[j] = nums[j], nums[i]
            helper(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
            
    helper(nums, 0)
    return lst

print(all_permutations([1, 2, 3]))