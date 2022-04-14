"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        sol = []
    
        def preord(node):
            if node:
                sol.append(node.val)
                
                for c in node.children:
                    preord(c)
        
        preord(root)
        return sol
            