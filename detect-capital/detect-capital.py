class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            haslower = False
            hasupper = False
            
            for i in word[1:]:
                if i.islower():
                    haslower = True
                elif i.isupper():
                    hasupper = True
                if haslower and hasupper:
                    return False
        else:
            for i in word[1:]:
                if i.isupper():
                    return False
                
        
        return True