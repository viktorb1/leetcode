# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def depth(p):
            if not p: return 0
            left = depth(p.left)
            right = depth(p.right)
            maxdepth = max(left, right)
            self.ans = max(self.ans, left + right)
            return 1 + maxdepth

        depth(root)
        return self.ans