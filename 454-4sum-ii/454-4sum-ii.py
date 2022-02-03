class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        last = dict()
        count = 0
        
        for n3 in nums3:
            for n4 in nums4:
                if n3+n4 in last:
                    last[n3+n4] += 1
                else:
                    last[n3+n4] = 1
            
        for one in nums1:
            for two in nums2:
                if -(one + two) in last:
                    count += last[-(one + two)]
                        
        return count