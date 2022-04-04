class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                break
                
            for ele in row:
                if ele > target:
                    break
                
                if ele == target:
                    return True
        
        return False