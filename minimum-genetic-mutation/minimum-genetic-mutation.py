class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # print(self.hasSingleDifference('AACCGCTA', 'AAACGGTA'))
        return self.dfs(start, end, bank, 0)
        
    
    def dfs(self, cur, end, bank, output):
        print(cur, end, bank, output)
        if cur == end:
            return output
        
        ans = float('inf')
        
        for idx, b in enumerate(bank):
            if self.hasSingleDifference(cur, b):
                x = self.dfs(b, end, bank[:idx] + bank[idx+1:], output+1)
                
                if x >= 0:
                    ans = min(x, ans)
                    
        return -1 if ans == float('inf') else ans
        
        
        
    def hasSingleDifference(self, cur, nex):
        count = 0
        
        for i in range(len(nex)):
            if cur[:i] + nex[i] + cur[i+1:] == nex and cur != nex:
                count += 1
        print(count)
        return True if count == 1 else False