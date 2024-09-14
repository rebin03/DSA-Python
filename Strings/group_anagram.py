def group_anagrams(strings):
    
    if len(strings) == 0:
        return []
    
    new_lst = [''.join(sorted(string)) for string in strings]
    ht = {}
    
    for i in range(len(strings)):
        
        if new_lst[i] in ht:
            ht[new_lst[i]].append(strings[i])
        else:
            ht[new_lst[i]] = [strings[i]]
        
    return list(ht.values())