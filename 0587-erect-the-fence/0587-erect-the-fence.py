class Solution:
    def outerTrees(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def cross_prod(x, y, z):
            a, b, c, d, e, f = x[0], x[1], y[0], y[1], z[0], z[1]
            return (f-b)*(c-a) - (d-b)*(e-a)

        if len(points) < 3: return points
        two = first = min(points, key = lambda point: (point[0], point[1])) # get leftmost
        hull = [two]

        while True:
            most_counter = []
            i = 0

            for three in points:
                if three == two:
                    continue
                if not most_counter: 
                    most_counter = [three]
                    continue

                c = cross_prod(two, three, most_counter[-1])
                
                if c > 0:
                    i = 0
                    most_counter = [three]
                elif c == 0:
                    if dist(two, most_counter[i]) < dist(two, three):
                        i = len(most_counter)

                    most_counter.append(three)

            hull += most_counter
            if most_counter[i] == first: break
            two = most_counter[i]

        return set(tuple(h) for h in hull)
