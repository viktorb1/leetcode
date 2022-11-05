class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo: return memo[i]
            largest_length = 1
            count = 1
            
            for j in range(i-1, -1, -1):
                cur_len, cur_count = dfs(j)
                if nums[j] < nums[i]:
                    if cur_len + 1 > largest_length:
                        largest_length = max(largest_length, cur_len + 1)
                        count = cur_count
                    elif cur_len + 1 == largest_length:
                        count += cur_count
                    
            memo[i] = [largest_length, count]
            return [largest_length, count]
        
        
        for i in range(len(nums)-1, -1, -1):
            dfs(i)
        
        largest = max(memo.values(), key=lambda x: x[0])[0]
        return sum([x[1] for x in memo.values() if x[0] == largest])