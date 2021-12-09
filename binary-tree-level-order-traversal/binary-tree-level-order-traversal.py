# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        sol = [[root]]
        s = [[root.val]]
    
        while sol[-1] != []:
            level = []

            for node in sol[-1]:
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)
                    
            sol.append(level)
            s.append([x.val for x in level])
        
        return s[:-1]

        
        
        