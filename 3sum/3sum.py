from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        counts = Counter(nums)
        
        
        for i in range(len(nums)):
            first = nums[i]
            counts[first] -= 1
            
            for j in range(i+1, len(nums)):
                second = nums[j]
                counts[second] -= 1
                third = -(first + second)
                
                if third in counts and counts[third] > 0:
                    ans.add(tuple(sorted((first, second, third))))
                
                counts[second] += 1
                 
            counts[first] += 1

        
        return ans