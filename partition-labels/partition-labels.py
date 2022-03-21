class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        starts, ends = dict(), dict()
        
        for i, c in enumerate(s):
            if c not in starts:
                starts[c] = i
            ends[c] = i

        intervals = sorted([[starts[c], ends[c]] for c in starts], key=lambda x: x[0])
        sol = []
        
        newInterval = intervals[0]
        for interval in intervals[1:]:
            if newInterval[1] >= interval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            else:
                sol.append(newInterval)
                newInterval = interval
        
        sol.append(newInterval)
        return [i[1]-i[0]+1 for i in sol]