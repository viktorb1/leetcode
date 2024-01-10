# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        stack = [(root, None)]
        while stack:
            n, p = stack.pop()
            
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)
            if n.left:
                stack.append((n.left, n))
            if n.right:
                stack.append((n.right, n))
        
        print(graph)
        
        q = deque([start])
        seen = {start}
        ans = 0
        
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                for y in graph[x]:
                    if y not in seen:
                        seen.add(y)
                        q.append(y)
            ans += 1
        return ans - 1