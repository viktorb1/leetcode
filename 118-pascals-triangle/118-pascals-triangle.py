class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(numRows - 1):
            curr = [0] + triangle[i] + [0]
            next = []
            
            for i in range(len(curr) - 1):
                next.append(curr[i] + curr[i+1])
            
            triangle.append(next)
                            
        return triangle