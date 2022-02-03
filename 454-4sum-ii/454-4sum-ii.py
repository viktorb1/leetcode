class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        last = defaultdict(int)
        count = 0
        
        for three in nums3:
            for four in nums4:
                last[three+four] += 1
            
        for one in nums1:
            for two in nums2:
                count += last[-(one + two)]
                        
        return count