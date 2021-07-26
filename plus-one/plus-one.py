class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1
        if digits[last] < 9:
            digits[last] += 1
        else:
            j = last
            
            while digits[j] == 9:
                digits[j] = 0
                j -= 1
                    
            if j == -1:
                return [1] + digits
            else:
                digits[j] += 1
        
        return digits
