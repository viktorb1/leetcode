class Solution:
    def numDecodings(self, s: str) -> int:
        dic = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'}
        memo = {}
        
        def helper(s):
            if not s:
                return 1
            elif s in memo:
                return memo[s]
            
            total = 0
            
            if s[0] in dic:
                total += helper(s[1:])
            
            if len(s) > 1 and s[0:2] in dic:
                total += helper(s[2:])
                
            memo[s] = total
            return total
        
        return helper(s)