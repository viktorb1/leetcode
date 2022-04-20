class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        g = defaultdict(list)
        for e1, e2 in edges:
            g[e1].append(e2)
            g[e2].append(e1)

        leaves = [node for node in g if len(g[node]) == 1]
        sol = []
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for l in leaves:
                val = g[l].pop()
                g[val].remove(l)
                if len(g[val]) == 1:
                    newLeaves.append(val)
            leaves = newLeaves
        
        return leaves