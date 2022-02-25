class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(c for c in 'aeiouAEIOU')
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            
            while left < right and s[right] not in vowels:
                right -= 1
                
            if left >= right:
                break
            
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left += 1
            right -= 1
        
        return s