class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        nums = []
        
        # create an array out of the integer
        while x > 0:
            nums.append(x % 10)
            x //= 10
        
        # loop through half the array, check if the first and last int is the same
        for i in range(len(nums) // 2):
            end = len(nums) - i - 1
            
            if nums[i] != nums[end]:
                return False
        
            end -= 1
        
        
        return True
            
            
            
            