# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root)
    
    def inorder(self, root):
        if not root: return
        sol = []
        if root.left: sol += self.inorder(root.left)
        if root: sol += [root.val]
        if root.right: sol += self.inorder(root.right)
        return sol