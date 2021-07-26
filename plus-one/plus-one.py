class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1
        if digits[last] < 9:
            digits[last] += 1
        else:
            for i in range(len(digits) - 1, -1, -1 ):
                if digits[i] == 9:
                    digits[i] = 0;
                    
                    if i == 0:
                        return [1] + digits
                else:
                    digits[i] += 1
                    break
        
        return digits