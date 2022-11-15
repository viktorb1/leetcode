
class Solution:
    def removeStones(self, points):
        seen = set()
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for i, (x,y) in enumerate(points):
            rows[x].append(i)
            cols[y].append(i)
        
        def dfs(x, y):
            count = 1
            seen.add((x,y))
            
            for r in rows[x]:
                if tuple(points[r]) not in seen:
                    count += dfs(points[r][0], points[r][1])
            
            for c in cols[y]:
                if tuple(points[c]) not in seen:
                    count += dfs(points[c][0], points[c][1])
            
            return count
    
        total = 0
        for x,y in points:
            if (x,y) not in seen:
                total += dfs(x, y) - 1
        return total