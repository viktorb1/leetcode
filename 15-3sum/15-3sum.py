class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i, n in enumerate(nums[:-2]):
            if i > 0 and n == nums[i-1]:
                continue
            
            second =  i + 1
            third = len(nums) -1
            while second < third:
                summ = n + nums[second] + nums[third]
                if summ < 0:
                    second += 1
                elif summ > 0:
                    third -= 1
                else:
                    ans.add((n, nums[second], nums[third]))
                    second += 1
                    
        return ans