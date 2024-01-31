class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]: 
                p = stack.pop()
                ans[p] = i - p
            stack.append(i)
        
        return ans
# you can think of T[i] pointer as moving faster than the stack pointer
# this stack removes everything smaller than T[i]
# this means that the values in the stack have not seen anything bigger than themselves until T[i] (which means it's the next greatest element)
# this is an example of a monotonic decreasing stack since we are removing everything smaller than itself before add it