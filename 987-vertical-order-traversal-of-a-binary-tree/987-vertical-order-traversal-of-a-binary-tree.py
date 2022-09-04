# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        nex = []
        sol = defaultdict(list)
        
        while queue:       
            queue = sorted(queue, key=lambda x: (x[1], x[0].val))
            
            for n, x in queue:
                sol[x].append(n.val)
                if n.left: nex.append((n.left, x-1))
                if n.right: nex.append((n.right, x+1))

            queue = nex
            nex = []
        
        return [sol[k] for k in sorted(sol)]