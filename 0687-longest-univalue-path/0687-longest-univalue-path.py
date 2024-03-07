# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        dist1 = self.longestUnivaluePath(root.left)
        dist2 = self.longestUnivaluePath(root.right)
        hl = self.height(root.left, root.val) + 1 if root.left and root.left.val == root.val else 0
        hr = self.height(root.right, root.val) + 1 if root.right and root.right.val == root.val else 0
        return max(dist1, dist2, hl+hr)

    def height(self, node, val):
        if not node: return 0
        l, r = 0, 0
        if node.left and node.left.val == val:
            l = 1 + self.height(node.left, val)

        if node.right and node.right.val == val:
            r = 1 + self.height(node.right, val)

        return max(l, r)