class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        sol = []
        
        a, b = points[0][0], points[0][1]
        
        for (c,d) in points:
            if b >= c:
                a, b = max(a, c), min(b, d)
            else:
                sol.append((a,b))
                a, b = c, d

        sol.append((a,b))
        return len(sol)
