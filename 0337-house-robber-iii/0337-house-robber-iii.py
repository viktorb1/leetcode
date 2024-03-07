# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def inorder(node, must_skip=False):
            if not node: return 0

            a = node.val + inorder(node.left, True) + inorder(node.right, True) if not must_skip else 0
            b = inorder(node.left) + inorder(node.right)
            return max(a, b)
        
        return max(inorder(root), inorder(root, True))