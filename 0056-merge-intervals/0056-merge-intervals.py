class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        intervals = sorted(intervals, key=lambda x: x[0])
        cur = intervals[0]

        for j, i in enumerate(intervals[1:]):
            if cur[0] > i[1]:
                sol.append(i)
            elif cur[1] < i[0]:
                sol.append(cur)
                if j + 1 < len(intervals):
                    cur = intervals[j+1]
            else:
                cur = [min(cur[0], i[0]), max(cur[1], i[1])]
        
        sol.append(cur)
        return sol
                
            