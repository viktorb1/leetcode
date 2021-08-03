class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for i in nums:
            if not i in seen:
                print("adding", i)
                seen.add(i)
            else:
                return True
            
        return False