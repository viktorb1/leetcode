class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        saw = set()
        
        for i in nums:
            if i in saw:
                saw.remove(i)
            else:
                saw.add(i)
        
        return saw.pop()