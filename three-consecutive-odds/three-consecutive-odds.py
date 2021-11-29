class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            if num % 2 == 0:
                count = 0
            elif num % 2 == 1:
                count += 1
            
            if count == 3:
                return True
            
        
        return False
            
                