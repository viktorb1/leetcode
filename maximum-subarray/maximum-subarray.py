class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            if nums[i-1] >= 0:
                nums[i] += nums[i-1]
        
        return max(nums)
    
    
    
 



# O(n^2)
def max_sum_brute(nums):
    max_sum = float('-inf')

    for i in range(len(nums)):
        cur_sum = 0
        
        for num in nums[i:]:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)

    return max_sum


# O(n) - dynamic programming
def kadanes_algorithm(nums):

    global_max = float('-inf')
    local_max = 0

    for num in nums:
        local_max = max(local_max + num, num)
        global_max = max(global_max, local_max)

    return global_max


# O(n)
def cross(nums):
    m = len(nums) // 2
    left, right = 0, 0
    max_left, max_right = 0, 0

    for num in nums[m::-1]:
        left += num
        max_left = max(left, max_left)

    for num in nums[m+1:]:
        right += num
        max_right = max(right, max_right)

    return max_left + max_right


# O(nlogn) - divide and conquer algorithm
def divide_n_conquer(nums):
    if len(nums) == 1:
        return nums[0]
    
    l = divide_n_conquer(nums[:len(nums)//2])
    r = divide_n_conquer(nums[len(nums)//2:])
    c = cross(nums)
    return max(l, r, c)
