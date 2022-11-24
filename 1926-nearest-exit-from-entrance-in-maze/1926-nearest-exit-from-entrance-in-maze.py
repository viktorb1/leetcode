class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance[0], entrance[1], 0)])
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        
        while q:
            i, j, dist = q.popleft()
            
            if dist > 0 and (i in [0, m-1] or j in [0, n-1]):
                return dist
            
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                    maze[x][y] = '+'
                    q.append((x, y, dist+1))
        
        
        return -1