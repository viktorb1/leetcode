class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(n, i) for i, n in enumerate(nums)], key=lambda x: x[0])
        
        for i in range(len(nums)-1):       
            j = i+1
            while j < len(nums) and nums[j][0] - nums[i][0] <= t:
                if abs(nums[j][1] - nums[i][1]) <= k:
                    return True
                
                j += 1