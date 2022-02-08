class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        
        for w in words:
            for i in range(1, len(w)):
                words_set.discard(w[i:])
               
        count = 0
        for w in words_set:
            count += len(w) + 1
        
        return count