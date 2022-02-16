class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        used = set()
        remove = 0
        
        for c in count:
            while count[c] > 0 and count[c] in used:
                count[c] -= 1
                remove += 1
            used.add(count[c])
        
        return remove
                
            