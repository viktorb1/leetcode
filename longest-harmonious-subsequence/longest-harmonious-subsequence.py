class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        s = sorted(list(set(nums)))
        maxLen = 0
        
        for i1, i2 in zip(s, s[1:]):
            if i1 + 1 == i2:
                maxLen = max(maxLen, c[i1] + c[i2])
        
        return maxLen