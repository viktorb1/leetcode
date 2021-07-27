class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0

        for j in range(0, n):
            
            i = start #since the array is sorted, you don't have to check anything before what you've checked already 
            
            while i < m and nums1[i] < nums2[j]:
                i +=  1
            
            start = i + 1

            for k in range(m-1, i-1, -1):
                nums1[k+1] = nums1[k]

            nums1[i] = nums2[j]
            m += 1
