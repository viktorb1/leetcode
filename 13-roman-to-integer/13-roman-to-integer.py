class Solution:
    def romanToInt(self, s: str) -> int:
        
        output = 0
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for c, cn in zip(s, s[1:]):
            if val[c] < val[cn]:
                output -= val[c]
            else:
                output += val[c]
        
        output += val[s[-1]]
        return output
                