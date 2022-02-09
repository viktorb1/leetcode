class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        
        for p in pieces:
            dic[p[0]] = p
        
        res = []
        
        for num in arr:
            if num in dic:
                res += dic[num]
            
        return res == arr