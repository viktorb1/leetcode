class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur = intervals[0]
        count = 1
        
        for x,y in intervals[1:]:
            if x >= cur[1]:
                cur = [x,y]
                count += 1
        
        return len(intervals) - count