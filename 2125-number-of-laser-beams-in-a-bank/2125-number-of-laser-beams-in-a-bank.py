class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cur = 0
        prev = 0
        total = 0
        
        for r in bank:
            for c in r:
                if c == '1':
                    cur += 1

            total += prev * cur
            prev = cur if cur else prev
            cur = 0
        
        return total