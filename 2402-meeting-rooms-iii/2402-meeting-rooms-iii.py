class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        occupied = []
        available = [i for i in range(n)]
        count = [0] * n
        meetings.sort()
        
        for s, e in meetings:
            while occupied and s >= occupied[0][0]:
                _, room = heappop(occupied)
                heappush(available, room)
            
            if available:
                room = heappop(available)
                heappush(occupied, (e, room))
            else:
                end, room = heappop(occupied)
                heappush(occupied, (end + (e-s), room))
            
            count[room] += 1
        
        return count.index(max(count))