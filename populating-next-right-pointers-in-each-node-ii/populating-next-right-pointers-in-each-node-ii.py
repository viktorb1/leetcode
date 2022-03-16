"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root]) if root else []
        nex = deque([])
        
        while q:
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            
            while q:
                x = q.popleft()
                if x.left: nex.append(x.left)
                if x.right: nex.append(x.right)
            
            q = nex
            nex = deque([])
            
        return root