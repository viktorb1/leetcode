# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                sol.append(node)
                inorder(node.right)
        
        sol = []
        inorder(root)
        for i in range(len(sol)-1):
            sol[i].left = None
            sol[i].right = sol[i+1]
        sol[-1].left = None
        sol[-1].right = None
        return sol[0] if sol else None