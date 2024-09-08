def two_sum(array,target):
    
    hash_table = {}
    
    for i, n in enumerate(array):
        val = target - n
        
        if val in hash_table:
            return [hash_table[val], i]
        
        hash_table[n] = i
                
    return []
            
        


print(two_sum([2,-1,5,3],4))