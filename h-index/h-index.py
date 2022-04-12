class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxCitations = 0
        for i in range(1, len(citations)+1):
            num = 0
            
            for c in citations:
                if c >= i:
                    num += 1
            
            if num >= i:
                maxCitations = i
                
        
        return maxCitations