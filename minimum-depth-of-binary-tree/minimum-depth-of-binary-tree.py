# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0;
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            
            if left > 0 and right > 0:
                return 1 + min(left, right)
            elif left == 0:
                return 1 + right
            else:
                return 1 + left
    