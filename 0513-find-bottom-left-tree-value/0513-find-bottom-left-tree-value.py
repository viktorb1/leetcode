# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val

        queue = deque([root])
        leftmost = None
        
        while queue:
            set_val = False
            for i in range(len(queue)):
                n = queue.popleft()
                if not set_val:
                    if n.left:
                        leftmost = n.left.val
                        set_val = True
                    elif n.right:
                        leftmost = n.right.val
                        set_val = True
                
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
        
        return leftmost