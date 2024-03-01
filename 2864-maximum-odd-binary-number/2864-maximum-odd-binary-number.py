class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = sum([1 for i in s if i=='1'])
        return '1'*(ones_count-1) + '0'*(len(s)-ones_count) + '1'