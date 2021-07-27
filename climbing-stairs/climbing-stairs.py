class Solution:
    def climbStairsHelper(self, i: int, n: int, memo: List[int]) -> int:
         
        if i > n: # we went out of bounds, so it's not a valid sequence
            return 0
        elif i == n:
            return 1 # we stayed in bounds, so it's a valid sequence to climb the stairs
        elif memo[i] > 0: # previously calculated values, 'memoization'
            return memo[i]
        else:
            memo[i] = self.climbStairsHelper(i+1, n, memo) + self.climbStairsHelper(i+2, n, memo)
            return memo[i]
        
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        return self.climbStairsHelper(0, n, memo)
        
