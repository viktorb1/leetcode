class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        seen = {}
        
        @cache
        def dfs(node, path):
            if node == len(graph) - 1:
                sol.append(path)
                return
                        
            for i in graph[node]:
                dfs(i, path + tuple([i]))
        
        dfs(0, tuple([0]))
        return sol