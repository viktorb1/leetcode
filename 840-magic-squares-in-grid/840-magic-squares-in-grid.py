class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagicSquare([g[j:j+3] for g in grid[i:i+3]]):
                    count += 1
        return count
        
    def isMagicSquare(self, grid):
        if sorted([val for row in grid for val in row]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
        rows = [sum(row) for row in grid]
        cols = [sum(row[i] for row in grid) for i in range(len(grid[0]))]
        diag = [sum(grid[i][i] for i in range(len(grid)))] 
        diag += [grid[2][0] + grid[1][1] + grid[0][2]]
        return len(set(rows + cols + diag)) == 1