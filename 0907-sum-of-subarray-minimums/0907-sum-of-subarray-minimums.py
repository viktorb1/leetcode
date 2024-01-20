class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        res = 0
        
        for i in range(len(arr)): # for each Right Hand Side
            while stack and arr[stack[-1]] > arr[i]: # keep popping while value in stack is greater than RHS
                mid = stack.pop()
                left = stack[-1]
                right = i
                res += arr[mid] * (mid - left) * (right - mid)
            
            stack.append(i)

        return res % (10 ** 9 + 7)