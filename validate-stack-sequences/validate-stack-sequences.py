class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        
        while i < len(pushed) and j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
            
        while j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        
        return True if not stack else False