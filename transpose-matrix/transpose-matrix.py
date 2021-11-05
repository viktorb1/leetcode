class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix[0])
        tp = []
        
        for i in range(row_len):
            new_row = []
            for row in matrix:
                new_row.append(row[i])
            
            tp.append(new_row)
            
        return tp
                