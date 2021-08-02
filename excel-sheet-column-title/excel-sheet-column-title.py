class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
                        
        sol = ""
        
        while columnNumber > 0:
            sol += chr(ord('A') + (columnNumber - 1) % 26)
            columnNumber -= (columnNumber - 1) % 26
            columnNumber //= 26
        
        return sol[::-1]
