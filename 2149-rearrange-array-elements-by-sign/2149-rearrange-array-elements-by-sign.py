from queue import Queue

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        
        return [item for pair in zip(pos, neg) for item in pair]