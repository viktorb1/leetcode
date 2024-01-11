class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def postorder(node):
            nonlocal ans

            if not node:
                return float('inf'), float('-inf')

            l_sm, l_lg = postorder(node.left)
            r_sm, r_lg = postorder(node.right)

            node_min = min(l_sm, r_sm, node.val)
            node_max = max(l_lg, r_lg, node.val)

            max_diff = max(
                abs(node.val - node_min),
                abs(node.val - node_max)
            )

            ans = max(max_diff, ans)
            return node_min, node_max

        postorder(root)
        return ans
