class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        sum_nums = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if abs(total - target) < diff:
                    diff = abs(total - target)
                    sum_nums = total

                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return sum_nums