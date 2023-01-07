from math import atan, atan2, pi
from typing import List, Tuple

class Solution:
    def outerTrees(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def angle(a, b, c):
            angle = (atan2(a[0]-b[0],a[1]-b[1]) - atan2(c[0]-b[0],c[1]-b[1])) * 180/pi
            return angle if angle < 180 else (angle - 360)

        if len(points) < 3: return points
        two = first = min(points, key = lambda point: point[0]) # get leftmost
        one = (two[0], two[1]+1) # doesn't matter what we set it to, as long as it's not equal to `two`
        hull = [two]

        while True:
            ang = float('inf')
            smallest = []

            for three in points:
                if three in [one, two]:
                    continue
                
                a = angle(one, two, three)
                if a < ang:
                    ang = a
                    smallest = [three]
                elif a == ang:
                    smallest.append(three)

            hull += smallest
            if smallest[0] == first: break
            one, two = two, smallest[0]

        return set(tuple(h) for h in hull)