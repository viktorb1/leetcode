# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def traverse(root):
            nonlocal count
            if not root:
                return -1

            traverse(root.left)
            ans.append(root.val)
            count += 1

            if count == k:
                return

            traverse(root.right)
            
        
        ans = []
        traverse(root)
        return ans[k-1]
