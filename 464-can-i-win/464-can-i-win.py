class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        choices = tuple(i for i in range(1, maxChoosableInteger+1))
        
        @cache
        def can_win(cur_sum, choices):
            if cur_sum + choices[-1] >= desiredTotal:
                return True

            for j, num in enumerate(choices):
                if not can_win(cur_sum + num, choices[:j] + choices[j+1:]):
                    return True
            
            return False
        
        if sum(choices) < desiredTotal:
            return False
        
        return can_win(0, choices)