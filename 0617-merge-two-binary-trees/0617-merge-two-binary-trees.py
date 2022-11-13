import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursive(root1, root2)
    
    def recursive(self, node1, node2):
        if node1 and node2:
            root = TreeNode(node1.val + node2.val)
            root.left = self.recursive(node1.left, node2.left)
            root.right = self.recursive(node1.right, node2.right)
            return root
        else:
            return copy.deepcopy(node1) if node1 else copy.deepcopy(node2)