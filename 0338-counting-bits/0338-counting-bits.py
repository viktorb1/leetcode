class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0, 1] if n >=1 else [0]
        cur = 0
        power = 2
        
        for _ in range(n-1):
            if cur == power:
                cur = 0
                power *= 2
            
            sol.append(sol[cur]+1)
            cur += 1
        
        return sol