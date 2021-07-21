# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':     
        # we couldn't find any value
        if not root:
            return None
        
        # we found either p or q
        if root == q or root == p:
            return root

        
        # left is null if p or q doesn't exist in the left side of the tree
        # otherwise, p or q are returned to left if found in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
       
        # the code below evaluates once we know what values left and right are
        # if both sides have values then by definition of lca, we know that the current node is the lca
        # if only right or left had a value, then we keep passing that value up the tree
        if left and right: # both sides had values
            return root
        elif left: # only the left side has values
            return left
        elif right: # only the right side had values
            return right
        else:
            return None
