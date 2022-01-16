class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        output = []
        
        def backtrack(nums, path):
            if len(path) == k:
                output.append(path)
                return
            elif len(path) > k:
                return
            else:
                for i in range(len(nums)):
                    backtrack(nums[i+1:], path + [nums[i]])
        
        backtrack(nums, [])
        return output