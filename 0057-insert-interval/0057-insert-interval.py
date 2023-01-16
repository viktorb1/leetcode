class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        smaller = [i for i in intervals if i[1] < newInterval[0]]
        larger = [i for i in intervals if i[0] > newInterval[1]]
        
        if len(smaller + larger) < len(intervals):
            newInterval[0] = min(intervals[len(smaller)][0], newInterval[0])
            newInterval[1] = max(intervals[-len(larger)-1][1], newInterval[1])
        
        return smaller + [newInterval] + larger