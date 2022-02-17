# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxVal = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMax(root):
            if not root:
                return 0

            x = max(getMax(root.left), 0)
            y = max(getMax(root.right), 0)
            self.maxVal = max(self.maxVal, x + root.val + y) 
            return root.val + max(x, y)
        getMax(root)
        return self.maxVal