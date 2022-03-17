# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            nonlocal sums
            if not node.left and not node.right: 
                sums += total
            if node.left: 
                dfs(node.left, (total*10) + node.left.val)
            if node.right: 
                dfs(node.right, (total*10) + node.right.val)
        
        sums = 0
        if root: dfs(root, root.val)
        return sums