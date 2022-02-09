class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        
        for i, word in enumerate(l, 1):
            if searchWord == word[:len(searchWord)]:
                return i
        
        return -1