# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root: return 0
            left = height(root.left)
            right = height(root.right)
            self.longest_path = max(self.longest_path, left + right)
            return 1 + max(left, right)
        self.longest_path = 0
        height(root)
        return self.longest_path