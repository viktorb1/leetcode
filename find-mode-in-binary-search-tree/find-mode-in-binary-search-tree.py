# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root:
                inorder(root.left)
                nums[root.val] += 1
                inorder(root.right)
                
        nums = defaultdict(int)
        nums[float('-inf')] = float('-inf')
        inorder(root)
        sol = [float('-inf')]
                
        for n in nums:
            if nums[n] > nums[sol[-1]]:
                sol = [n]
            elif nums[n] == nums[sol[-1]]:
                sol += [n]
            
        return sol
            