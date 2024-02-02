class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, h = 0, len(nums1)
        total = len(nums1) + len(nums2)
        mid = (total+1) // 2
        
        # nums1 must be shorter than num2 because if it's not then it would be possible that m > mid 
        # which wouldn't make sense for mid-m
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) 
        
        # we are doing binary search on the partitions
        # m is the partition of nums1 and mid-m is the partition of nums2
        while l <= h:
            m = (l + h) // 2
            
            # if the partitions make something out of bounds, we let it pass through our if statements on line 24
            r1 = nums1[m-1] if 0 < m <= len(nums1) else float('-inf')
            l1 = nums1[m] if 0 <= m < len(nums1) else float('inf')
            r2 = nums2[mid-m-1] if 0 < mid-m <= len(nums2) else float('-inf')
            l2 = nums2[mid-m] if 0 <= mid-m < len(nums2) else float('inf')
            
            # r1 <= l1 automatically since nums1 is sorted, same for r2 <= l2
            if r1 <= l2 and r2 <= l1:
                if total % 2 == 0:
                    return (max(r1, r2) + min(l2, l1)) / 2
                else:
                    return max(r1, r2)
            elif r1 > l2:
                h = m - 1
            else:
                l = m + 1

