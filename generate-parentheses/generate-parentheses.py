class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, ans, [], 0, 0)
        return ans
    
    def dfs(self, n, ans, item, left, right):
        if 2*n == len(item):
            ans.append("".join(item))
            return
        
        if left < n:
            self.dfs(n, ans, item + ['('], left+1, right)
        
        if right < left:
            self.dfs(n, ans, item + [')'], left, right+1)
