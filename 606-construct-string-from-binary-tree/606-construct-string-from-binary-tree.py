# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)[1:-1]
    
    def preorder(self, root):
        if not root:
            return
        
        res = f"({root.val}"
        
        if root.left:
            res += f"{self.preorder(root.left)}"
        elif root.right:
            res += "()"
        
        if root.right:
            res += f"{self.preorder(root.right)}"
        
        return f"{res})"