class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sol = ""
        count = 0
        
        for end in range(len(s)-1, -1, -1): 
            while count < len(s) and not s[count].isalpha():
                sol += s[count] 
                count += 1
                
            if s[end].isalpha():
                count += 1
                sol += s[end]
            
            while count < len(s) and not s[count].isalpha():
                sol += s[count] 
                count += 1
            
        return sol
            
                
                
            