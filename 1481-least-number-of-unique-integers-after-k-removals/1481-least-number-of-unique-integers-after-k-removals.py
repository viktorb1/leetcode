from queue import PriorityQueue

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        unique_count = len(c)
        pq = PriorityQueue()
        
        for key, val in c.items():
            pq.put((val, key))
        
        while not pq.empty():
            val, key = pq.get()
            
            if k >= val:
                unique_count -= 1
                k -= val
            else:
                break
        
        return unique_count