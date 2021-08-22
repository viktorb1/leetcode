class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        saw = {}
        
        for i, v in enumerate(nums):
            if v in saw and i - saw[v] <= k:
                return True
            else:
                saw[v] = i
        
        return False