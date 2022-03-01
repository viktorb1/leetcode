class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        choices = tuple(i for i in range(1, maxChoosableInteger+1))
        
        @cache
        def play_game(cur_sum, choices):
            if cur_sum + choices[-1] >= desiredTotal:
                return True

            for j, num in enumerate(choices):
                if not play_game(cur_sum + num, choices[:j] + choices[j+1:]):
                    return True
            
            return False
        
        if sum(choices) < desiredTotal:
            return False
        
        return play_game(0, choices)