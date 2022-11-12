# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentx, depthx = self.inorder(root, x)
        parenty, depthy = self.inorder(root, y)
        return parentx != parenty and depthx == depthy
        
    def inorder(self, node, find, prev=None, level=0):
        if not node:
            return None
        elif node.val == find:
            return (prev, level)
        
        x = self.inorder(node.left, find, node, level+1)
        y = self.inorder(node.right, find, node, level+1)
        return x if x else y