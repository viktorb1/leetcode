class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        sol = []
        
        for i in range(len(grid[0])):
            x, y = i, 0
            
            while y < len(grid):
                if (x == 0 and grid[y][x] == -1) or (x == len(grid[0])-1 and grid[y][x] == 1):
                    sol.append(-1)
                    break
                elif grid[y][x] == 1 and grid[y][x+1] != -1:
                    y += 1
                    x += 1
                elif grid[y][x] == -1 and grid[y][x-1] != 1:
                    y += 1
                    x -= 1
                else:
                    sol.append(-1)
                    break
            
            if y == len(grid):
                sol.append(x)
                
        return sol
                