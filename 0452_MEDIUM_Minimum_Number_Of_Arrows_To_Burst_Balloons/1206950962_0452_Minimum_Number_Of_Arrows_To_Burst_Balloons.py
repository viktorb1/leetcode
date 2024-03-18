class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        count = 0
        a, b = points[0][0], points[0][1]
        
        for (c,d) in points:
            if b >= c:
                a, b = max(a, c), min(b, d)
            else:
                count += 1
                a, b = c, d

        return count + 1