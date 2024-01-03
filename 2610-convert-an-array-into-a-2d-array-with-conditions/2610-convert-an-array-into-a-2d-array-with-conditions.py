from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = [[] for _ in range(max(count.values()))]
                
        for num, num_seen in count.items():
            for i in range(num_seen):
                res[i].append(num)
        
        return res
                