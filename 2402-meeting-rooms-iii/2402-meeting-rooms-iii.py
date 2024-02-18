class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        occupied = []
        available = [i for i in range(n)]
        count = [0] * n
        meetings.sort()
        
        for s, e in meetings:
            while occupied and s >= occupied[0][0]: # put all meetings that ended back into available
                end, room = heappop(occupied)
                heappush(available, room)
            
            if available: # use the lowest number room if a room is free
                room = heappop(available)
                heappush(occupied, (e, room))
            else: # use the room that ends the soonest if all rooms are taken
                time, room = heappop(occupied)
                heappush(occupied, (time + (e - s), room))
            
            count[room] += 1
        
        return count.index(max(count))