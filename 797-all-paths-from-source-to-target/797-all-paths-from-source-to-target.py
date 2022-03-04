class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        seen = {}
        
        @cache
        def dfs(path):
            if path[-1] == len(graph) - 1:
                sol.append(path)
                return
                        
            for i in graph[path[-1]]:
                dfs(path + tuple([i]))
        
        dfs(tuple([0]))
        return sol