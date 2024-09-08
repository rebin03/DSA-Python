def isomorphic_strings(s, t):
    
    if len(s) != len(t):
        return False
        
    hash_s = {}
    hash_t = {}

    for i in range(len(s)):
        ch_s = s[i]
        ch_t = t[i]

        if ch_s not in hash_s:
            hash_s[ch_s] = ch_t

        if ch_t not in hash_t:
            hash_t[ch_t] = ch_s

        if hash_s[ch_s] != ch_t or hash_t[ch_t] != ch_s:
                return False
    
    return True

print(isomorphic_strings('aacad','bbdbe'))