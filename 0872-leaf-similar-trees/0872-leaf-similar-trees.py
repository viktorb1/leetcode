# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def inorder(node, leafnodes):
            if not node: return
            
            inorder(node.left, leafnodes)
            
            if not node.left and not node.right:
                leafnodes.append(node.val)
            
            inorder(node.right, leafnodes)          
        
        l1, l2 = [], []
        inorder(root1, l1)
        inorder(root2, l2)
        
        return l1 == l2