class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sol = []
        
        for i in range(1, ceil(sqrt(area))+1):
            if area % i == 0:
                if (i > area // i):
                    sol.append([i , area // i])
                else:
                    sol.append([area // i, i])
                
        return sol[-1]