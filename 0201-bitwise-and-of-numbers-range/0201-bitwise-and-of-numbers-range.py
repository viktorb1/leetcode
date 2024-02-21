class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        if len(left) != len(right): return 0
        
        num = 0
        for i in range(len(left)): 
            if left[i] == right[i] == '1':
                num += pow(2, len(left)-i-1)
            elif left[i] != right[i]:
                break
        
        return num

# same as longest common prefix of both binary numbers (because those are the only digits that don't change)
# the rest will change from 0 to 1 to 0 as you increment