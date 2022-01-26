# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1 = self.inorder(root1)
        root2 = self.inorder(root2)
        sol = []
        x, y = 0, 0
        
        while x < len(root1) and y < len(root2):
            if root1[x] < root2[y]:
                sol.append(root1[x]) 
                x += 1
            else:
                sol.append(root2[y])
                y += 1
        
        sol += root1[x:]
        sol += root2[y:]
        return sol
        
        
    def inorder(self, root):
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)