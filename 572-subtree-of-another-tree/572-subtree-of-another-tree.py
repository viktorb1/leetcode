# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.checkEquality(root, subRoot):
            return True
        
        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        
    def checkEquality(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.checkEquality(root.left, subRoot.left) and self.checkEquality(root.right, subRoot.right)

        