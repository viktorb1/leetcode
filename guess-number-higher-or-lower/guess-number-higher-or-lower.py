# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        pick = n // 2
        high = n
        
        while 1:
            if guess(pick) == 1:
                low = pick + 1
                pick = (low + high) // 2
            elif guess(pick) == -1:
                high = pick - 1
                pick = (low + high) // 2
            elif guess(pick) == 0:
                return pick