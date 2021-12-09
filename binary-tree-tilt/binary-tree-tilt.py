# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        tilt = abs(self.getSum(root.right) - self.getSum(root.left))
        tilt += self.findTilt(root.right) 
        tilt += self.findTilt(root.left)
        return tilt
    
    def getSum(self, root):
        if not root:
            return 0
        
        return root.val + self.getSum(root.left) + self.getSum(root.right)