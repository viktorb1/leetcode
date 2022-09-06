# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder(root)
        return root if self.calc_sum(root) > 0 else None
    
    def inorder(self, root):
        if self.calc_sum(root.left):
            self.inorder(root.left)
        else:
            root.left = None
        
        if self.calc_sum(root.right):
            self.inorder(root.right) 
        else:
            root.right = None
        
    def calc_sum(self, root):
        if not root: return 0
        total = root.val
        
        if root.left: 
            total += self.calc_sum(root.left)
        if root.right: 
            total += self.calc_sum(root.right)
        
        return total
        