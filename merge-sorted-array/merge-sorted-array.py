class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for j in range(0, n): 
            
            i = 0
            
            while i < m and nums1[i] < nums2[j]:
                i +=  1

            for k in range(m-1, i-1, -1):
                nums1[k+1] = nums1[k]

            nums1[i] = nums2[j]
            m += 1
                
            