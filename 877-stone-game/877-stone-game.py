class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        target = sum(piles) // 2 + 1
        
        @cache
        def dfs(piles, target):
            if target <= 0:
                return True
            elif not piles:
                return False
            
            if dfs(piles[2:], target-piles[0]) \
            or dfs(piles[1:-1], target-piles[0]) \
            or dfs(piles[1:-1], target-piles[-1]) \
            or dfs(piles[:-2], target-piles[-1]):
                return True
                        
            return False
        
        return dfs(tuple(piles), target)