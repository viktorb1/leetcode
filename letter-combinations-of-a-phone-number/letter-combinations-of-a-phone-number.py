from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        chars = [char_map[i] for i in digits]
        return [''.join(x) for x in product(*chars)] if digits != "" else []