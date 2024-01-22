class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        z = set([i+1 for i in range(len(nums))])
        seen = set()
        ans = []
        
        for n in nums:
            if n in seen:
                ans.append(n)
            z.discard(n)
            seen.add(n)
        
        ans.append(z.pop())
        return ans