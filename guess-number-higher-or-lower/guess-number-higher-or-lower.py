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
    
# Alternative solution
# More messy to read, but faster due to binary search implementation
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        i = num // 8
        high = num
        
        
        while 1:
            if i*i == num:
                return True
            elif i*i < num:
                if (i+1)*(i+1) > num:
                    return False
                
                low = i + 1
                i = (low + high) // 2
                
            elif i*i > num:
                if (i-1)*(i-1) < num:
                    return False
                
                high = i - 1
                i = (low + high) // 2
        
        
        return False
