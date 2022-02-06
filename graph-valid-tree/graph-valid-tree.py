class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        adj = {i:set() for i in range(n)}

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        seen = set()

        def dfs(n, prev):
            if n in seen:
                return False

            seen.add(n)

            for v in adj[n]:
                if v != prev:
                    if not dfs(v, n):
                        return False

            return True
        
        return dfs(0, -1) and len(seen) == len(adj)