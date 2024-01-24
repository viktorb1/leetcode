from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node, c):
            nonlocal count
            
            if not node.left and not node.right:
                if self.is_palindrome(c):
                    count += 1
            
            if node.left:
                c[node.left.val] += 1
                dfs(node.left, c)
                c[node.left.val] -= 1
            
            if node.right:
                c[node.right.val] += 1
                dfs(node.right, c)
                c[node.right.val] -= 1
        
        dfs(root, Counter([root.val]))
        return count
            
    def is_palindrome(self, c):
        return len([d for d in c.values() if d % 2 == 1]) <= 1