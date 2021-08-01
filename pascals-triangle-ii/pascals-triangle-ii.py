class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        startRow = [1]
        nextRow = []
        
        for i in range(rowIndex):
            curr = [0] + startRow + [0]
            
            for j in range(len(curr)-1):
                nextRow.append(curr[j] + curr[j+1])
                            
            startRow = nextRow.copy()
            nextRow.clear()
            
        
        return startRow
            