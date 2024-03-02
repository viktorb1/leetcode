class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0])+1)
        ans = 0
        
        for row in matrix:
            for i, n in enumerate(row):
                if n == '1': heights[i] += 1
                else: heights[i] = 0
            
            stack = []
            
            for i, n in enumerate(heights):
                start = i
                
                while stack and stack[-1][1] > n:
                    h_start, height = stack.pop()
                    w = i - h_start
                    ans = max(ans, w * height)
                    start = h_start
                
                stack.append((start, n))
        
        return ans