def getDuplicate(nums):
    hare = 0
    tortoise = 0
    
    while True:
        
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        
        if tortoise == hare:
            pointer = 0
            
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]
            
            return pointer
        
print(getDuplicate([4, 3, 1, 2, 3]))