class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        
        for i, val in enumerate(heights):
            j = i
            
            while stack and stack[-1][1] > val:
                index, height = stack.pop()
                width = i - index
                area = max(area, height * width)
                j = index
            
            stack.append((j, val))
            
        for i, val in stack:
            area = max(area, val * (len(heights) - i))
            
        return area
                
            
            