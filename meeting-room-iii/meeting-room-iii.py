class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meetingRoomIII(self, intervals, rooms, ask):
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        hours = max(ends)
        hours_track = []
        i, j = 0, 0
        cur_rooms_in_use = 0

        for h in range(hours+1):
            while i < len(starts) and h == starts[i]:
                cur_rooms_in_use += 1
                i += 1
            while j < len(ends) and h == ends[j]:
                cur_rooms_in_use -= 1
                j += 1
            hours_track.append(cur_rooms_in_use)
        
        ans = []
        for a in ask:
            if all(hours_track[i] < rooms for i in range(a[0], a[1])):
                ans.append(True)
            else:
                ans.append(False)

        return ans

