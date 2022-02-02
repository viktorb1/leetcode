class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        right_zeros = s.count('0')
        left_ones = 0
        res = left_ones + right_zeros
        
        for c in s:
            if c == '0':
                right_zeros -= 1
            
            if c == '1':
                left_ones += 1
            
            res = min(res, left_ones + right_zeros)
        
        return res
            