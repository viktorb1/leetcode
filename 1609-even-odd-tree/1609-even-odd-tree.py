# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        is_odd = False
        
        while q:
            prev = None
            for _ in range(len(q)):
                n = q.popleft()
                if n.val % 2 == is_odd:
                    return False
                if prev and is_odd and prev <= n.val:
                    return False
                if prev and not is_odd and prev >= n.val:
                    return False
                if n.left: 
                    q.append(n.left)
                if n.right: 
                    q.append(n.right)
                prev = n.val
            is_odd = not is_odd
        
        return True