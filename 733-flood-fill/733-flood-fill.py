class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque()
        q.append((sr, sc))
        oldval = image[sr][sc]
        
        if image[sr][sc] == newColor:
            return image
        
        while q:
            r, c = q.popleft()
            image[r][c] = newColor
            
            for x, y in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= x < len(image) and 0 <= y < len(image[0]):
                    if image[x][y] == oldval:
                        q.append((x, y))
        
        return image