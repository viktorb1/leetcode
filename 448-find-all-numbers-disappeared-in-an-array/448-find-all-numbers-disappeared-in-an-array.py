class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        size = len(nums)
        diff = size*(size+1)//2 - sum(s)
        sol = []
        
        for i in range(1, size+1):
            if i not in s:
                sol.append(i)
        
        return sol