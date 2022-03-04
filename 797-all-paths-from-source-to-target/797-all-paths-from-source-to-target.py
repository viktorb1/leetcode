class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        seen = {}
        
        def dfs(path):
            if path[-1] == len(graph) - 1:
                sol.append(path)
                return
                        
            for i in graph[path[-1]]:
                dfs(path + [i])
        
        dfs([0])
        return sol