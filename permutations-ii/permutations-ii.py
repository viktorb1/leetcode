class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.choose([], nums, ans)
        return ans
    
    def choose(self, perm, fr, ans):
        if len(fr) == 0 and perm not in ans:
            ans.append(perm)
        else:
            for idx, val in enumerate(fr):
                self.choose(perm + [val], fr[:idx] + fr[idx+1:], ans)