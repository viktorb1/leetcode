# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True

        if not left or not right or left.val != right.val:
            return False
        
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)