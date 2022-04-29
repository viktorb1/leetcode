class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(node):
            for n in graph[node]:
                if n not in color:
                    color[n] = 1 - color[node]
                    if not dfs(n):
                        return False
                else:
                    if color[node] == color[n]:
                        return False
            
            return True
        
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
                
        return True