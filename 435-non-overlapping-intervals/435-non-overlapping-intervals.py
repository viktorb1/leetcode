class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        sol = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] >= sol[-1][1]:
                sol.append(interval)
            
            
        return len(intervals) - len(sol)
                