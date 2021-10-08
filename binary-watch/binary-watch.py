from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        poss = [80, 40, 20, 10, 32, 16, 8, 4, 2, 1]
        sol = []
        
        for i in combinations(poss, turnedOn):
            hour = 0
            minute = 0
            
            for j in i:
                if j % 10 == 0:
                    hour += j // 10
                else:
                    minute += j
                
            if hour < 12 and minute < 60:
                sol.append(f'{hour}:{minute:02}')
        
        return sol
