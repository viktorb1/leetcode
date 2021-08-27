class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        total = 0

        for i in counts:
            if counts[i] % 2 == 0:
                total += counts[i]
            else:
                total += counts[i] - 1
                
        for i in counts:
            if counts[i] % 2 == 1:
                total += 1
                break
            
        return total
