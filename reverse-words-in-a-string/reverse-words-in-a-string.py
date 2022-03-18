class Solution:
    def reverseWords(self, s: str) -> str:
        s = [x for x in reversed(s.split(' ')) if x != ''] 
        return ' '.join(s)
