"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        cur = [root] if root else []
        nex = []
        sol = []
        
        while cur:
            sol.append([c.val for c in cur])

            for item in cur:
                for child in item.children:
                    if child:
                        nex.append(child)
            
            cur = nex
            nex = []
    
        return sol