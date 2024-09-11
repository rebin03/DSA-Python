def non_repeating_char(string):
    
    ht = {}
    
    for ch in string:
        
        if ch in ht:
            ht[ch] += 1
        else:
            ht[ch] = 1
            
    for i in range(len(string)):
        
        if ht[string[i]] == 1:
            return i
        
    return None

st = "sbdsbenkbs"
print(non_repeating_char(st))