# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_level, nex_level = [root], []
        sol = []
        
        while cur_level and cur_level[0]:
            sol.append([node.val for node in cur_level])
            for node in cur_level:
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)
            cur_level = nex_level
            nex_level = []
                
        return sol