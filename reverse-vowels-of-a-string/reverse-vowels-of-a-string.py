class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
#       vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
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
            
                
                
