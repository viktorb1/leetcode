class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        added = False
        
        for i in nums1:
            for j in range(len(nums2)):
                if nums2[j] == i:
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            sol.append(nums2[k])
                            added = True
                            break
                       
                    if not added:
                        sol.append(-1) 
                    
                    added = False
                
                       
        return sol
                            
                    

            