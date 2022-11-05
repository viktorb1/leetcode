class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for n in nums]
        sums = defaultdict(int)
        
        for i in range(len(nums)):
            largest_length = 1
            count = 1
            
            for j in range(i-1, -1, -1):
                cur_len, cur_count = dp[j]
                if nums[j] < nums[i]:
                    if cur_len + 1 > largest_length:
                        largest_length = max(largest_length, cur_len + 1)
                        count = cur_count
                    elif cur_len + 1 == largest_length:
                        count += cur_count
                    
            dp[i] = [largest_length, count]
            sums[largest_length] += count
        
        
        return sums[max(sums)]