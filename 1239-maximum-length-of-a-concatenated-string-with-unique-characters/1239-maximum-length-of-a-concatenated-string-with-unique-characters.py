class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [a for a in arr if len(set(list(a))) == len(list(a))] # remove duplicates
        dp = [set()]
        
        for a in arr:
            s1 = set(a)
            for s2 in dp:
                if not s1 & s2:
                    dp.append(s1.union(s2))
        
        return max([len(a) for a in dp])