# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        q = [[root]]
        
        while q[-1]:
            nex = []
            for node in q[-1]:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            
            if not nex: break
            q.append(nex)
        
        return [row[-1].val for row in q]