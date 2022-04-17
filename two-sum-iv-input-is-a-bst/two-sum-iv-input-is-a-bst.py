# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def inorder(node):
            if node:
                if inorder(node.left): return True
                if k - node.val in seen: return True
                seen.add(node.val)
                if inorder(node.right): return True
        
        return inorder(root)