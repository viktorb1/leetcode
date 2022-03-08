# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root:
                nonlocal res, prev
                inorder(root.left)
                if prev:
                    res = min(res, abs(root.val - prev.val))
                prev = root
                inorder(root.right)
        
        res = float('inf')
        prev = None
        inorder(root)
        return res
                