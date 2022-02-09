class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        have = set(arr) - {0}
        
        for ele in arr:
            if ele * 2 in have:
                return True
        
        if arr.count(0) > 1:
            return True
        
        return False