class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        
        for _ in range(2, numRows + 1):
            row = []
            
            for i, j in zip([0] + output[-1] + [0], output[-1] + [0]):
                row.append(i+j)
                
            output.append(row)
        
        return output