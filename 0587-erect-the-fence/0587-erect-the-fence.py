from math import atan, atan2, pi
from typing import List, Tuple

class Solution:
    def outerTrees(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def angle(a, b, c):
            angle = (atan2(a[0]-b[0],a[1]-b[1]) - atan2(c[0]-b[0],c[1]-b[1])) * 180/pi
            return angle if angle < 180 else (angle - 360)

        if len(points) < 3: return points
        points = [tuple(p) for p in points]
        two = first = min(points, key = lambda point: point[0])
        one = (two[0], two[1]+1) # doesn't matter what we set it to, as long as it's not equal to two
        hull = {two}

        while True:
            smallest = None
            ang = float('inf')
            same = []

            for three in points:
                if three in (one, two):
                    continue
                a = angle(one, two, three)

                if a < ang:
                    smallest = three
                    ang = a
                    same = [three]
                elif a == ang:
                    same.append(three)

            hull = hull.union(same)
            if smallest == first: break
            one, two = two, smallest

        return hull