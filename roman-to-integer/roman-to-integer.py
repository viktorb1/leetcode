class Solution:
    def romanToInt(self, s: str) -> int:
        
        x = 0
        i = 0
        convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        subtract = {'IV': 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        while i < len(s):
                if i < len(s) - 1 and s[i] + s[i+1] in subtract:
                    x += subtract[s[i] + s[i+1]] 
                    i += 2
                else:
                    x += convert[s[i]]
                    i += 1
                
        return x
                