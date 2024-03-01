class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = sum([int(i) for i in s])
        return '1'*(ones_count-1) + '0'*(len(s)-ones_count) + '1'