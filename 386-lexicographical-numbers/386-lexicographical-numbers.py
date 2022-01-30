class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        out = [1]
        
        while len(out) < n:
            num = out[-1]*10
            
            while num > n:
                num //= 10
                num += 1
                
                while num % 10 == 0:
                    num //= 10
            
            out.append(num)
        
        return out
