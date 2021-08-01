class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        startRow = [1]
        
        for i in range(rowIndex):
            startRow = [0] + startRow + [0]
            
            for j in range(len(startRow)-1):
                startRow[j] = startRow[j] + startRow[j+1]    
            
            startRow.pop()
        
        return startRow
