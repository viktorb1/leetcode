class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        sols = []
        
        def dfs(rem_s, sol):
            if len(sol) > 4:
                return
            
            if len(sol) == 4 and not rem_s:
                sols.append('.'.join(sol))
                return
            
            if rem_s:
                dfs(rem_s[1:], sol + [rem_s[0:1]])
            
            if len(rem_s) > 1 and rem_s[0] != '0':
                dfs(rem_s[2:], sol + [rem_s[0:2]])
        
            if len(rem_s) > 2 and int(rem_s[0:3]) < 256 and rem_s[0] != '0':
                dfs(rem_s[3:], sol + [rem_s[0:3]])
        
        dfs(s, [])
        return sols