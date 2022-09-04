from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        nex = []
        sol = defaultdict(list)
        
        while queue:       
            for n, x in queue:
                sol[x].append(n.val)
                if n.left: nex.append((n.left, x-1))
                if n.right: nex.append((n.right, x+1))
            
            nex = sorted(nex, key=lambda x: (x[1], x[0].val))
            queue = nex
            nex = []
        
        return [sol[k] for k in sorted(sol)]