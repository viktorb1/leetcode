from math import atan2, pi

class Solution:
    def outerTrees(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def angle(a, b, c):
            AB = (a[0] - b[0], a[1] - b[1])
            AC = (c[0] - b[0], c[1] - b[1])
            dot_prod = AB[0] * AC[0] + AB[1] * AC[1]
            deg = degrees(atan2(AB[0] * AC[1] - AB[1] * AC[0], dot_prod))
            return deg if deg != 180 else -180

        if len(points) < 3: return points
        points = [tuple(p) for p in points]
        two = first = min(points, key = lambda point: point[0])
        one = (two[0], two[1]+1)
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

            if smallest == first:
                break

            one, two = two, smallest


        return hull
