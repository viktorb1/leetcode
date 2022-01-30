class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        out = [1]
        
        while len(out) < n:
            prev = out[-1]
            
            if 10 * prev <= n:
                out.append(prev * 10)
            else:
                while (prev + 1) > n or (prev + 1) % 10 == 0:
                    prev //= 10
                    
                out.append(prev + 1)
        
        return out
