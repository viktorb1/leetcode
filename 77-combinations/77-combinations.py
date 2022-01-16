class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        output = []
        
        def backtrack(nums, path):
            if len(path) == k:
                output.append(path)
            else:
                for idx, num in enumerate(nums):
                    backtrack(nums[idx+1:], [num] + path)
        
        backtrack(nums, [])
        return output