from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if len(digits) == 0:
            return []
        
        ans = deque()
        
        # initially add all letters from first digit (the seed)
        for l in char_map[digits[0]]:
            ans.append(l)
            
        # loop through the remaining digits
        for l, d in enumerate(digits[1:], 1):
            while len(ans[0]) == l:
                x = ans.popleft()
                for i in char_map[d]:
                    ans.append(x + i)
        
        return ans
