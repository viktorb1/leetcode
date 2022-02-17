# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def pathRun(root):
            if not root:
                return 0

            left = max(pathRun(root.left), 0)
            right = max(pathRun(root.right), 0)
            self.ans = max(self.ans, left + root.val + right)
            return root.val + max(left, right)
        pathRun(root)
        return self.ans