class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        sol = []
        opts = Counter(digits)
        
        for num in range(100, 1000, 2):
            counts = Counter([int(c) for c in str(num)])
            
            for c in counts:
                if counts[c] > opts[c]:
                    break
            else:
                sol.append(num)
        
        return sol