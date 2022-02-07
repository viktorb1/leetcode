class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur = intervals[0]
        count = 0

        for interval in intervals[1:]:
            if interval[0] >= cur[1]:
                cur = interval
            else:
                count += 1
            
            
        return count