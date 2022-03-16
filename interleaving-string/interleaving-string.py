class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def dfs(s3, p1, p2):
            if not s3:
                return True
            elif p1 < len(s1) and p2 < len(s2) and s1[p1] == s3[0] and s2[p2] == s3[0]:
                return dfs(s3[1:], p1+1, p2) or dfs(s3[1:], p1, p2+1)
            elif p1 < len(s1) and s1[p1] == s3[0]:
                return dfs(s3[1:], p1+1, p2)
            elif p2 < len(s2) and s2[p2] == s3[0]:
                return dfs(s3[1:], p1, p2+1)
            else:
                return False
        
        return dfs(s3, 0, 0)