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
        delete, _ = self.inorder(root)
        return root if not delete else None
        
    def inorder(self, node, total = set()):
        if not node: return (None, [])
        if not node.left and not node.right:
            total = total.union({node})
            row_sum = sum([n.val for n in total])
            should_delete = self.limit > row_sum
            return (should_delete, [row_sum])
            
        delete_left, sums_left = self.inorder(node.left, total.union({node}))
        delete_right, sums_right = self.inorder(node.right, total.union({node}))
        
        if delete_left: node.left = None
        if delete_right: node.right = None
                                             
        combined = sums_left + sums_right
        should_delete = all(self.limit > val for val in sums_left + sums_right)
        return (should_delete, sums_left + sums_right)