class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lower = 0
        
        for c in word:
            if c.isupper():
                upper += 1
            else:
                lower += 1
        
        return (upper == len(word)) or (upper == 1 and word[0].isupper()) or upper == 0
