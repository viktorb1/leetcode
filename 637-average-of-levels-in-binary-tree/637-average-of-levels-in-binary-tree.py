# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from statistics import mean

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        nex = []
        solution = []
        
        while queue:
            solution.append(mean(q.val for q in queue))
            
            for val in queue:
                if val.left: nex.append(val.left)
                if val.right: nex.append(val.right)
            
            queue = nex
            nex = []
            
        return solution