from queue import PriorityQueue

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        q = PriorityQueue()
        for i, (start, end) in enumerate(times):
            q.put((start, 1, i))
            q.put((end, 0, i))
        
        chair = [0] * len(times)
        picked_chairs = {}
        
        while not q.empty():
            _, which, i = q.get()
            
            if which == 1:
                idx = chair.index(0)
                
                if i == targetFriend:
                    return idx
                
                chair[idx] = 1
                picked_chairs[i] = idx
            else:
                chair[picked_chairs[i]] = 0
                
        
        return -1