class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sol = []
        
        i = 1
        
        while i*i <= area:
            if area % i == 0:
                if (i > area // i):
                    sol.append([i , area // i])
                else:
                    sol.append([area // i, i])
            i += 1
                
        
        return sol[-1]
