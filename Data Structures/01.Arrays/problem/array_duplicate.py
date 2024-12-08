class Solution:
    def findDuplicates(self, arr):
        
        dicts = {}
        
        for n in arr:
            if n in dicts:
                dicts[n] += 1
            else:
                dicts[n] = 1
                
        res = []
        for k, v in dicts.items():
            if v > 1:
                res.append(k)
                
        res.sort()   
        return res