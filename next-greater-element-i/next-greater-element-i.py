class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        
        for x in nums2:
            while len(st) and st[-1] < x: # when you run into an upcoming value that is larger than all those in the stack
                d[st.pop()] = x # set all numbers in stack to the upcoming value, x
            st.append(x) # keep adding all numbers to the stack

        for x in range(len(nums1)):
            nums1[x] = d.get(nums1[x], -1)
            
        return nums1
