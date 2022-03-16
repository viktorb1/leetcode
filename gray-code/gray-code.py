class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = [0]
        
        i = 0
        while len(codes) < pow(2, n):
            codes += [x + pow(2, i) for x in codes[::-1]]
            i += 1
    
        return codes
            
                
            
            