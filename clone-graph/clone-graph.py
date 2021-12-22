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
        
        deq = deque([node])
        clone_map = {node : Node(node.val)}
        
        while deq:
            cur = deq.popleft()
            
            for n in cur.neighbors:
                if n not in clone_map:
                    deq.append(n)
                    clone_map[n] = Node(n.val)
                
                clone_map[cur].neighbors.append(clone_map[n])
                    
        return clone_map[node]