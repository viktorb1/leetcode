class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sol = []
    
        for i in range(len(str(low)), len(str(high)) + 1):
            x = deque([j+1 for j in range(i)])
            
            while x[-1] <= 9:  
                n = self.int(x)
                
                if n >= low and n <= high:
                    sol.append(n)

                x.popleft()
                x.append(x[-1] + 1)
            
        return sol
        
    def int(self, x):
        y = 0

        for i in x:
            y *= 10
            y += i

        return y