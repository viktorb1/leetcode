"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:   
        if not root: return 0
        maxdepth = 0
        for c in root.children:
            maxdepth = max(maxdepth, self.maxDepth(c))
            
        return 1 + maxdepth