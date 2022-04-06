class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dfs(e):
            if e.isdigit():
                return [int(e)]
            
            res = []
            for i, c in enumerate(e):
                if c in '*+-':
                    left = dfs(e[:i])
                    right = dfs(e[i+1:])
                    for l in left:
                        for r in right:
                            if c == '*':
                                res.append(l*r)
                            elif c == '+':
                                res.append(l+r)
                            elif c == '-':
                                res.append(l-r)

            return res
        
        return dfs(expression)