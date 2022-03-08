# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
            
        nodes = []
        inorder(root)
        print([node.val for node in nodes])
        a, b = 0, len(nodes)-1
        
        while a < len(nodes) - 1:
            if nodes[a].val > nodes[a+1].val:
                break
            else:
                a += 1
        
        while b >= 1:
            if nodes[b-1].val > nodes[b].val:
                break
            else:
                b -= 1       
                
        nodes[a].val, nodes[b].val = nodes[b].val, nodes[a].val
                