# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, total):
            if not node.left and not node.right and total == targetSum:
                sols.append(path)
            
            if node.left:
                dfs(node.left, path + [node.left.val], total + node.left.val)
            
            if node.right:
                dfs(node.right, path + [node.right.val], total + node.right.val)
        
        sols = []
        if root: dfs(root, [root.val], root.val)
        return sols
        