class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [c[::-1] for c in s]
        return ' '.join(s)