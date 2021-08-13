class Solution:
    def constructRectangle(self, area: int) -> List[int]:        
        i = int(sqrt(area))
        
        while area % i != 0:
            i -= 1
        
        return [area // i, i]
