class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.choose([], sorted(nums), ans)
        return ans
    
    def choose(self, perm, fr, ans):
        if not fr:
            ans.append(perm)
        
        i = 0
        while i < len(fr):               
            self.choose(perm + [fr[i]], fr[:i] + fr[i+1:], ans)
            
            while i+1 < len(fr) and fr[i] == fr[i+1]:
                i += 1
            
            i += 1
