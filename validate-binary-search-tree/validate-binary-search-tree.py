# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True
        elif not low < root.val < high:
            return False
        else:
            return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)