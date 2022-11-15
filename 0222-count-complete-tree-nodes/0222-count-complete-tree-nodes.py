# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left, right = root, root
        height = 0
        
        while right:
            left = left.left
            right = right.right
            height += 1
        
        if not left:
            return 2**height - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)