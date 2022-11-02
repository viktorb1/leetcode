class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def differ_by_one(s1, s2):
            num_dif = 0

            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    num_dif += 1

            return True if num_dif == 1 else False
        
        res = float('inf')
        
        def dfs(cur, seen, count=0):
            nonlocal res
            seen.add(cur)

            if cur == end:
                res = min(res, count)
            else:
                for b in bank:
                    if b not in seen and differ_by_one(cur, b):
                        dfs(b, seen, count+1)
                        seen.discard(b)
        
        seen = set()
        cur = start
        dfs(cur, seen)
        return -1 if res == float('inf') else res
        