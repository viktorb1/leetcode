# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        
        while q:
            prev = None
            for _ in range(len(q)):
                n = q.popleft()
                if n.val % 2 == level % 2:
                    return False
                if prev and level % 2 and prev <= n.val:
                    return False
                if prev and not level % 2 and prev >= n.val:
                    return False
                if n.left: 
                    q.append(n.left)
                if n.right: 
                    q.append(n.right)
                prev = n.val
            level += 1
        
        return True