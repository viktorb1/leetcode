class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sol = []

        for n in nums:
            if nums[abs(n)-1] < 0:
                sol.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        
        return sol
