# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = deque([root] if root else [])
        sol = []
        
        while cur:
            row = []
            for i in range(len(cur)):
                x = cur.popleft()                 
                row.append(x.val)
                
                if x.left:
                    cur.append(x.left)
                if x.right:
                    cur.append(x.right)
                
            sol.append(row)
            
        return sol[::-1]
            