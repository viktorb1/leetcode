# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while 1:
            left = self.findVal(root.left, p, q)
            right = self.findVal(root.right, p, q)

            if left and right:
                return root
            elif left and (root == p or root == q):
                return root
            elif right and (root == p or root == q):
                return root
            elif left:
                root = root.left
            elif right:
                root = root.right
            else:
                return None
                
    
    def findVal(self, node, p, q):
        if not node:
            return False
        elif node == p or node == q:
            return True
        else:
            return self.findVal(node.left, p, q) or self.findVal(node.right, p, q)
            