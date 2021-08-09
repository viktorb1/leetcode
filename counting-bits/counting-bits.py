class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        
        for i in range(1, n+1):
            total = 0
            
            while i > 0:
                if i % 2 == 1:
                    total +=1
                
                i //= 2
            
            out.append(total)
        
        return out