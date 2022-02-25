class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        largestnum1 = 0
        largestnum2 = 0
        
        for i in range(1, int(sqrt(num+2))+1):
            if (num + 1) % i == 0:
                largestnum1 = i
            if (num + 2) % i == 0:
                largestnum2 = i
  
        if ((num+1)//largestnum1) - largestnum1 < ((num+2)//largestnum2) - largestnum2:
            return [(num+1)//largestnum1, largestnum1]
        else:
            return [(num+2)//largestnum2, largestnum2]
        