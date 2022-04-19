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
        i, j = 0, len(nodes)-1
        
        while i < len(nodes) - 1 and nodes[i].val < nodes[i+1].val:
            i += 1
        
        while j >= 1 and nodes[j-1].val < nodes[j].val:
            j -= 1       
                
        nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                