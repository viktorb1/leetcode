class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return self.dfs(start, end, bank, 0)
        
    
    def dfs(self, cur, end, bank, output):
        if cur == end:
            return output
        
        ans = -1
        
        for idx, b in enumerate(bank):
            if self.hasSingleDifference(cur, b):
                x = self.dfs(b, end, bank[:idx] + bank[idx+1:], output+1)
                
                if x >= 0:
                    ans = x if ans == -1 else min(x, ans)
        
        return ans
        
        
        
    def hasSingleDifference(self, cur, nex):
        count = 0
        
        for i in range(len(nex)):
            if cur[i] != nex[i]:
                count += 1

        return True if count == 1 else False
