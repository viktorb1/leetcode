class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        
        for i in (range(len(val)//2)):
            if (val[i] != val[len(val)-i-1]):
                return False
        
        return True
