# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def preorder(node, nums):
            if node:
                if node.val % 2 == 0:
                    if node.left and node.left.left: nums.append(node.left.left.val)
                    if node.left and node.left.right: nums.append(node.left.right.val)
                    if node.right and node.right.left: nums.append(node.right.left.val)
                    if node.right and node.right.right: nums.append(node.right.right.val)
                preorder(node.left, nums)
                preorder(node.right, nums)
        
        nums = []      
        preorder(root, nums)
        return sum(nums)