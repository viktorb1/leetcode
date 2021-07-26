class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        
        if digits[j] < 9:
            digits[j] += 1
        else:        
            while digits[j] == 9:
                digits[j] = 0
                j -= 1
                    
            if j == -1:
                return [1] + digits
            else:
                digits[j] += 1
        
        return digits
