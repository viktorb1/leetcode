class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, h = 0, len(nums1)
        total = len(nums1) + len(nums2)
        mid = (total+1) // 2
        
        # nums1 must be shorter than num2 because if it's not then it would be possible that m > mid 
        # which wouldn't make sense for mid-m
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) 
        
        while l <= h:
            m = (l + h) // 2
                        
            r1 = float('-inf') if m == 0 else nums1[m-1]
            l1 = float('inf') if m == len(nums1) else nums1[m]
            r2 = float('-inf') if mid-m == 0 else nums2[mid-m-1]
            l2 = float('inf') if mid-m == len(nums2) else nums2[mid-m]
            
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

