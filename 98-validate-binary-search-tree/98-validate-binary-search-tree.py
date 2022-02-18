# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minval=float('-inf'), maxval=float('inf')) -> bool:
        if not root:
            return True
        elif not minval < root.val < maxval:
            return False
        
        return self.isValidBST(root.left, minval, root.val ) and self.isValidBST(root.right, root.val, maxval)