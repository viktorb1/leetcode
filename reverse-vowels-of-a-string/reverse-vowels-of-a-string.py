class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ls = list(s)
        
        while start < end:
            while ls[start] not in vowels and start < end:
                start += 1
                        
            while ls[end] not in vowels and end > start:
                end -= 1
                            
            ls[start], ls[end] = ls[end], ls[start]
            start += 1
            end -= 1
        
        return ''.join(ls)
            
                
                