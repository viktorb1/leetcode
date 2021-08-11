class Solution:
    def toLowerCase(self, s: str) -> str:
        newstr = ""
        
        for i in s:
            if i >= "A" and i <= "Z":
                newstr += chr(ord(i) + 32)
            else:
                newstr += i
                
        return newstr