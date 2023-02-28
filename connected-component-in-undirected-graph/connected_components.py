class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            self.parent[parent_y] = parent_x

class Solution:
    def count_connected_comp(self):
        edges = [[1, 0], [0, 2], [5, 3], [3, 4], [6, 7]]
        uf = UnionFind(8)

        for x, y in edges:
            uf.union(x, y)

        return sum([1 if p == i else 0 for i, p in enumerate(uf.parent)])

print(Solution().count_connected_comp())