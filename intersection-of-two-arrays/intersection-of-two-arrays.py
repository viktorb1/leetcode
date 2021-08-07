class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        same = []
        
        for i in nums1:
            for j in nums2:
                if j == i and j not in same:
                    same.append(j)
                    break
                    
        return same