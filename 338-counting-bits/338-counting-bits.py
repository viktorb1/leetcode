class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0, 1] if n >= 1 else [0]
        curr = 0
        until = 2
        
        for i in range(2, n+1):
            if curr == until:
                curr = 0
                until *= 2
            
            sol.append(sol[curr] + 1)
            curr += 1
                
        return sol