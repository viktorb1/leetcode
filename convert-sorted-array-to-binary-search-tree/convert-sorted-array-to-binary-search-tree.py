# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None
        
        mid = len(nums)//2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[:mid]) 
        tree.right = self.sortedArrayToBST(nums[mid+1:])
                    
        return tree