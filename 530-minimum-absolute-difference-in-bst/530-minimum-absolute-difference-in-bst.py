# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                inord.append(root.val)
                inorder(root.right)
        
        inord = []
        inorder(root)
        res = float('inf')
        
        for n1, n2 in zip(inord, inord[1:]):
            res = min(res, n2 - n1)
        
        return res
                