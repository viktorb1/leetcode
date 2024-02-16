from queue import PriorityQueue

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        pq = PriorityQueue()
        
        for key, val in c.items():
            pq.put((val, key))
        
        while not pq.empty():
            val, key = pq.get()
            
            if k >= val:
                del c[key]
                k -= val
            else:
                break
        
        return len(c)