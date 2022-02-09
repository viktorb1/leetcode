class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        counts = Counter(nums)
        
        
        for n in nums:           
            if k != 0: 
                if n + k in counts:
                    ans.add((n, n+k))
                elif n - k in counts:
                    ans.add((n-k, n))
            else:
                if counts[n] > 1:
                    ans.add((n, n))
        
        return len(ans)