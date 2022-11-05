# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        self.paths = defaultdict(list)
        self.inorder(root)
        self.to_delete = set()
        
        for x, sums in self.paths.items():
            if all(y < limit for y in sums):
                self.to_delete.add(x)
        
        self.prune(root)
        return root if root not in self.to_delete else None
        
    def prune(self, node):
        if not node: 
            return
        if node.left and node.left in self.to_delete:
            node.left = None
        elif node.left:
            self.prune(node.left)
        
        if node.right and node.right in self.to_delete:
            node.right = None
        elif node.right:
            self.prune(node.right)
         
        
    def inorder(self, node, total = set()):
        if not node:
            return
        if not node or not node.left and not node.right:
            total = total.union({node})
            total_sum = sum([node.val for node in total])
            for node in total:
                self.paths[node].append(total_sum)
            return
        
        self.inorder(node.left, total.union({node}))
        self.inorder(node.right, total.union({node}))
        