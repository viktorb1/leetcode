class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur_int = intervals[0]
        count = 1
        
        for x,y in intervals[1:]:
            if cur_int[1] <= x:
                cur_int = [x,y]
                count += 1
        
        return len(intervals) - count