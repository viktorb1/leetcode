class Solution:
    def constructRectangle(self, area: int) -> List[int]:        
        i = ceil(sqrt(area))
        
        while area % i != 0:
            i -= 1
        
        return [area // i, i]
