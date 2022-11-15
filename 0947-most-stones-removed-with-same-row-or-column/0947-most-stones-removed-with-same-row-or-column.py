
class Solution:
    def removeStones(self, points):
        uf = {}
        
        def union(x, y):
            if x not in uf: uf[x] = x
            if y not in uf: uf[y] = y
            uf[find(x)] = find(y)
        
        def find(x):
            if uf[x] != x:
                return find(uf[x])
            return x
        
        for x, y in points:
            union(x, ~y)
        
        return len(points) - len(set(find(x) for x,y in points))
