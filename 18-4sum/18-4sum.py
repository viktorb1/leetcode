class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            one = nums[i]
            for j in range(i+1, len(nums)):
                two = nums[j]
                
                three = j + 1
                four = len(nums)-1

                while three < four:
                    summ = one + two + nums[three] + nums[four]

                    if summ < target:
                        three += 1
                    elif summ > target:
                        four -= 1
                    else:
                        ans.add((one, two, nums[three], nums[four]))
                        three += 1
                    
        return ans