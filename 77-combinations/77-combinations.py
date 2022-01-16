class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        output = []
        
        def backtrack(i, path):
            if len(path) == k:
                output.append(path)
                return
            else:
                for j in range(i, len(nums)):
                    backtrack(j+1, path + [nums[j]])
        
        backtrack(0, [])
        return output