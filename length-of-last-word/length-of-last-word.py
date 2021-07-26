class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        
        for i in reversed(s.rstrip()):
            if i == " ":
                return count

            count += 1
        
        return count
                