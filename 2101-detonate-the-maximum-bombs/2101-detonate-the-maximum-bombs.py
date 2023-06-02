from math import sqrt
from collections import deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxDetonated = 1
        
        for i, bomb1 in enumerate(bombs):
            count = 1
            exploded = deque([bomb1])
            seen = {i}
            
            while exploded:
                b = exploded.pop()
                for j, bomb2 in enumerate(bombs):
                    if i != j and j not in seen and self.isInRange(b, bomb2):
                        exploded.append(bomb2)
                        seen.add(j)
                        count += 1
            
            maxDetonated = max(count, maxDetonated)
        return maxDetonated
    
    def isInRange(self, bomb1, bomb2):
        distance = sqrt(pow(bomb2[1] - bomb1[1], 2) + pow(bomb2[0] - bomb1[0], 2))
        return distance <= bomb1[2]