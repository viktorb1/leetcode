class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        prev_bal = {0: -1}
        ans = 0

        for i, n in enumerate(nums):
            if n == 1:
                balance += 1
            else:
                balance -= 1
            
            if balance in prev_bal:
                ans = max(ans, i - prev_bal[balance])
            else:
                prev_bal[balance] = i
        
        return ans