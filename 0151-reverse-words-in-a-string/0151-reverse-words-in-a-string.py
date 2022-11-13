class Solution:
    def reverseWords(self, s: str) -> str:
        y = [x for x in s.split(" ") if x!= ""]
        return ' '.join(y[::-1])