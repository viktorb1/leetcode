from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = deque([""]) if len(digits) > 0 else deque()
        
        # loop through the remaining digits
        for l, d in enumerate(digits):
            while len(ans[0]) == l:
                x = ans.popleft()
                for i in char_map[d]:
                    ans.append(x + i)
        
        return ans
