class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        total = 1
        seenOdd = False
        
        for i in counts:
            if counts[i] % 2 == 0:
                total += counts[i]
            else:
                seenOdd = True
                total += counts[i] - 1
                
        if not seenOdd:
            total -= 1
            
        return total
        