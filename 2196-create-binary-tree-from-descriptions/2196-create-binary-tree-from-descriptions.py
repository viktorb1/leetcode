# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        
        for p, c, left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
    
        all_nodes = set(nodes.keys())
        for _, c, _ in descriptions:
            all_nodes.remove(c)
        
        [parent] = all_nodes
        return nodes[parent]