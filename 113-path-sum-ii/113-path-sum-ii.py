# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = []
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int, cur_path: int = []) -> List[List[int]]:
        if not root: return
        cur_path.append(root.val)

        if not root.left and not root.right and sum(cur_path) == targetSum:
            self.sol.append(cur_path.copy())
        
        self.pathSum(root.left, targetSum, cur_path)
        self.pathSum(root.right, targetSum, cur_path)
        cur_path.pop()
        return self.sol