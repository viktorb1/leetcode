# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def postorder(node):
            nonlocal ans
            
            if not node: return -1, -1
            
            l_sm, l_lg = postorder(node.left)
            r_sm, r_lg = postorder(node.right)
            
            if l_sm == -1: l_sm = node.val
            if l_lg == -1: l_lg = node.val
            if r_sm == -1: r_sm = node.val
            if r_lg == -1: r_lg = node.val
            
            max_diff = max(
                abs(node.val - l_sm), 
                abs(node.val - l_lg),
                abs(node.val - r_sm),
                abs(node.val - r_lg)
            )
            
            ans = max(max_diff, ans)
            return min(l_sm, r_sm, node.val), max(l_lg, r_lg, node.val)
    
        postorder(root)
        return ans