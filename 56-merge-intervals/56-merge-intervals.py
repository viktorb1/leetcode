class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        intervals.sort()
        
        newInterval = intervals[0]
        for interval in intervals[1:]:
            if newInterval[1] >= interval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            else:
                sol.append(newInterval)
                newInterval = interval
        
        sol.append(newInterval)
        return sol