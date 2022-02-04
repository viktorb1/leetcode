# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = deque([root] if root else [])
        nex = deque()
        sol = []
        
        while cur:
            row = []
            while cur:
                x = cur.popleft()                 
                row.append(x.val)
                
                if x.left:
                    nex.append(x.left)
                if x.right:
                    nex.append(x.right)
                
            sol.append(row)
            cur = nex
            nex = deque()
            
        return sol[::-1]
            