# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.binaryTreePathsHelper(root, [], "")
    
    def binaryTreePathsHelper(self, root: TreeNode, seen:List[str], newStr:str) -> List[str]:
        if not root.left and not root.right:  
            newStr += str(root.val)
            seen.append(newStr)
        else:
            newStr += str(root.val) + "->"
            
        if root.left:
            self.binaryTreePathsHelper(root.left, seen, newStr)
        if root.right:
            self.binaryTreePathsHelper(root.right, seen, newStr)        
        
        return seen