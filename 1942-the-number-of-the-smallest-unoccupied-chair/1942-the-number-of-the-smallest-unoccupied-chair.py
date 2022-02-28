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
            if i == targetFriend:
                return chair.index(0)
            elif which == 1:
                picked_chairs[i] = chair.index(0)
                chair[picked_chairs[i]] = 1
            else:
                chair[picked_chairs[i]] = 0
        
        return -1