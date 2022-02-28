class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        starts = sorted([(start, i) for i, (start, _) in enumerate(times)])
        ends = sorted([(end, i) for i, (_, end) in enumerate(times)])
        s, e = 0, 0
        chair = [0] * len(times)
        picked_chairs = {}
        
        while s < len(starts) and e < len(ends):
            if ends[e][0] <= starts[s][0]:
                chair[picked_chairs[ends[e][1]]] = 0
                e += 1
            elif starts[s][0] == times[targetFriend][0]:
                return chair.index(0)
            elif starts[s][0] < ends[e][0]:
                picked_chairs[starts[s][1]] = chair.index(0)
                chair[picked_chairs[starts[s][1]]] = 1
                s += 1
        
        return -1