class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sums_so_far = defaultdict(int)
        sums_so_far[0] = 1
        
        for n in nums:
            cum_sum += n
            
            if cum_sum - k in sums_so_far:
                count += sums_so_far[cum_sum-k]

            sums_so_far[cum_sum] += 1
            
            
        return count
        