class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        have = Counter(nums)
        
        if k == 0:
            count = 0
            
            for c in have:
                if have[c] > 1:
                    count += 1
            
            return count
        
        for n in nums:
            if n + k in have:
                ans.add((n, n+k))
            elif n - k in have:
                ans.add((n-k, n))
        
        return len(ans)