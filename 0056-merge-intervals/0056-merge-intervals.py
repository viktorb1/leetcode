class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = intervals[0]
        sol = []
        
        for i, (x,y) in enumerate(intervals[1:]):
            if cur[1] >= x:
                cur = [min(cur[0],x), max(cur[1],y)]
            else:
                sol.append(cur)
                cur = intervals[i+1]
                
        
        sol.append(cur)
        return sol