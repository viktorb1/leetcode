# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        # traverse tree
        # keep adding while less than targetSum or null
        if not root:
            return False
        
        targetSum -= root.val
        
        if targetSum == 0 and not root.left and not root.right:
            return True
         
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)     
