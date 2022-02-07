class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(t) - Counter(s)
        
        for c in counter:
            return c