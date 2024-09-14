def max_unique_length(string):
    
    start = 0
    seen = {}
    max_value = 0
    
    for i in range(len(string)):
        
        ch = string[i]
        
        if ch in seen:
            start = max(start, seen[ch]+1)
        
        max_value = max(max_value, i - start + 1)
        seen[ch] = i
        
    return max_value