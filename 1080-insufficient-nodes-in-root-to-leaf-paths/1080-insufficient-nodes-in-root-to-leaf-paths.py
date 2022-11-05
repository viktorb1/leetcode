# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        self.paths = defaultdict(list)
        self.limit = limit
        delete, _ = self.inorder(root, root.val)
        return root if not delete else None
        
    def inorder(self, node, total = 0):
        if not node: return (False, [])
        if not node.left and not node.right:
            should_delete = self.limit > total
            return (should_delete, [total])
            
        delete_left, sums_left = self.inorder(node.left, total + node.left.val if node.left else 0)
        delete_right, sums_right = self.inorder(node.right, total + node.right.val if node.right else 0)
        
        if delete_left: node.left = None
        if delete_right: node.right = None
                                             
        should_delete = all(self.limit > val for val in sums_left + sums_right)
        return (should_delete, sums_left + sums_right)