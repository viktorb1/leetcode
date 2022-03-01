class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        sol = set()
        
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and num >= 100:
                        sol.add(num)
        
        return sorted(list(sol))