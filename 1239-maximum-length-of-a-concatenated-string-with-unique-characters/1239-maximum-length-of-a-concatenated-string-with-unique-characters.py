class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [a for a in arr if len(set(list(a))) == len(list(a))] # remove duplicates
        dp = [set()]
        
        for a in arr:
            s1 = set(a)
            for i, s2 in enumerate(dp):
                if s1 & s2:
                    continue
                dp.append(s1.union(s2))
        
        return max([len(a) for a in dp])