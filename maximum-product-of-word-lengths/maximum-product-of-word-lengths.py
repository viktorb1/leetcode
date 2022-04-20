class Solution:
    def maxProduct(self, words: List[str]) -> int:
        count = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]).intersection(set(words[j])):
                    count = max(count, len(words[i])*len(words[j]))
                    
        return count