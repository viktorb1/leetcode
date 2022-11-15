
class Solution:
    def removeStones(self, points):
        visited = defaultdict(bool)
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for i, (x,y) in enumerate(points):
            rows[x].append(i)
            cols[y].append(i)
        
        def dfs(x, y):
            count = 1
            visited[(x,y)] = True
            
            for r in rows[x]:
                if not visited[tuple(points[r])]:
                    count += dfs(points[r][0], points[r][1])
            
            for c in cols[y]:
                if not visited[tuple(points[c])]:
                    count += dfs(points[c][0], points[c][1])
            
            return count
    
        total = 0
        for x,y in points:
            if not visited[(x,y)]:
                total += dfs(x, y) - 1
        return total