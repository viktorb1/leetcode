"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return
        
        q = deque({node})
        d = {node: Node(node.val)}
        
        while q:
            x = q.popleft()
            
            for n in x.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    q.append(n)
                
                d[x].neighbors.append(d[n])
        
        return d[node]