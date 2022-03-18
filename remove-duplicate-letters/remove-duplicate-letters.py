class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        visited = set()
        stack = []
        
        for c in s:
            if c not in visited:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                     visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
            count[c] -= 1
        
        return ''.join(stack)
                
            