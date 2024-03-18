class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval
        sol = []

        for i, (x,y) in enumerate(intervals):
            if a > y:
                sol.append((x,y))
            elif b < x:
                sol.append((a,b))
                return sol + intervals[i:]
            else:
                a, b = (min(x,a), max(y,b))

        sol.append((a,b))
        return sol