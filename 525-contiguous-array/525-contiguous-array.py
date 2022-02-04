class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cum_sum = 0
        max_len = 0
        d = dict({0: -1})
        
        for i, n in enumerate(nums):
            if n == 1:
                cum_sum += 1
            elif n == 0:
                cum_sum -= 1
                        
            if cum_sum in d:
                max_len = max(max_len, i - d[cum_sum])
            else:
                d[cum_sum] = i

                
        
        return max_len
            