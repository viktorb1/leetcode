class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        x, y = coordinates[0]
        i, j = coordinates[1]
        rise, run = j - y, i - x
        
        for (a, b), (c, d) in zip(coordinates[1:], coordinates[2:]):
            nex_rise, nex_run = d - b, c - a
            if rise * nex_run != run * nex_rise:
                return False
            
        return True