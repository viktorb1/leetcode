class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = [i for i in intervals if newInterval[0] > i[1]]
        right = [i for i in intervals if newInterval[1] < i[0]]
        
        if len(left) + len(right) < len(intervals):
            newInterval = [min(intervals[len(left)][0], newInterval[0]), max(intervals[-(len(right)+1)][1], newInterval[1])]

        return left + [newInterval] + right
        