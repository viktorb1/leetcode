class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse = True)
        vals = {s:i for i, s in enumerate(score)}
        score[vals[sorted_score[0]]] = "Gold Medal"
        
        if len(score) > 1:
            score[vals[sorted_score[1]]] = "Silver Medal"
        
        if len(score) > 2:
            score[vals[sorted_score[2]]] = "Bronze Medal"
        
        for i in range(3, len(sorted_score)):
            score[vals[sorted_score[i]]] = str(i+1)
        
        return score
            
            