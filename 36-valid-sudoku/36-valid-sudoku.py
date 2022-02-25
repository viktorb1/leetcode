class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each 3x3
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.checkThreeByThree([row[j:j+3] for row in board[i:i+3]]):
                    return False
        
        # check each row
        nums = set(list('0123456789'))
        
        for row in board:
            seen = set()

            for e in row:
                if e in nums:
                    if e in seen:
                        return False
                    else:
                        seen.add(e)
            
            seen = set()
            
        # check each col
        for i in range(len(board[0])):
            seen = set()
            
            for row in board:
                if row[i] in nums:
                    if row[i] in seen:
                        return False
                    else:
                        seen.add(row[i])
            
            seen = set()
        
        
        return True
            
                
                
    def checkThreeByThree(self, grid):
        nums = set(list('0123456789'))
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in nums:
                    if grid[i][j] in seen:
                        return False
                    else:
                        seen.add(grid[i][j])
        
        return True
            