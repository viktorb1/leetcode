class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1] if n > 0 else [0]
        curr = 0
        until = 2
        
        while len(ans) <= n:
            if curr == until:
                curr = 0
                until *= 2
            
            ans.append(ans[curr] + 1)
            curr += 1
        
        return ans
