"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        seen = set()
        sol = []

        def dfs(node, cg):
            if node in seen:
                return
            
            seen.add(node)
            cg.append(node.label)

            for n in node.neighbors:
                dfs(n, cg)
            
        sol = []
        for node in nodes:
            if node not in seen:
                cg = []
                dfs(node, cg)
                sol.append(sorted(cg))
        return sol