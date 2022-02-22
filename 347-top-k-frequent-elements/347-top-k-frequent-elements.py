from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        q = PriorityQueue()
        
        for c, v in count.items():
            q.put((-v, c))
            
        sol = []
        for _ in range(k):
            sol.append(q.get()[1])
            
        return sol