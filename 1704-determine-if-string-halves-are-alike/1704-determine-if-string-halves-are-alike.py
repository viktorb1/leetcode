class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = 0
        r = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        for i, c in enumerate(s):
            if i < len(s) // 2:
                if c in vowels:
                    l += 1
            else:
                if c in vowels:
                    r += 1
        
        return l == r