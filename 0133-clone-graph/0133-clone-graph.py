"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        q = deque([node])
        copies = {node: Node(node.val)}
        
        while q:
            cur = q.popleft()
            
            for n in cur.neighbors:
                if n not in copies:
                    copies[n] = Node(n.val)
                    q.append(n)
                
                copies[cur].neighbors.append(copies[n])
            
        return copies[node]