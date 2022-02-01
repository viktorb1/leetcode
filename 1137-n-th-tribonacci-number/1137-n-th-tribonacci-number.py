class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        first = 0
        second = 1
        third = 1
        
        for _ in range(3, n+1):
            forth = third + second + first
            first, second, third = second, third, forth
            
        return third