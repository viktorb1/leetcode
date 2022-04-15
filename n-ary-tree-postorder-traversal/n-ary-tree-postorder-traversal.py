"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        sol = []
        self.postord(root, sol)
        return sol
    
    def postord(self, node, sol):
        if node:            
            for c in node.children:
                self.postord(c, sol)
            
            sol.append(node.val)