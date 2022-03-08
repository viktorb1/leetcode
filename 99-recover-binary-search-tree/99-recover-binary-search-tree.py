# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root)
                inorder(root.right)
            
        nodes = []
        inorder(root)
        a, b = 0, len(nodes)-1
        
        while a < len(nodes) - 1 and nodes[a].val < nodes[a+1].val:
            a += 1
        
        while b >= 1 and nodes[b-1].val < nodes[b].val:
            b -= 1       
                
        nodes[a].val, nodes[b].val = nodes[b].val, nodes[a].val
                