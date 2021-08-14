class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        numCount = collections.Counter(nums)
        
        for i in numCount:
            count += (numCount[i])*(numCount[i]-1) // 2

        return count