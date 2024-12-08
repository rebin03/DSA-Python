class Solution:
    
    def nonRepeatingChar(self,s):
        
        ht = {}
        
        for ch in s:
            if ch in ht:
                ht[ch] += 1
            else:
                ht[ch] = 1
        
        for k, v in ht.items():
            if v == 1:
                return k
        return '$'