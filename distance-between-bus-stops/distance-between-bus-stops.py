class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if destination > start:
            return min(sum(distance[destination:len(distance)]) + sum(distance[0:start]), sum(distance[start:destination]))
        else:
            return min(sum(distance[start:len(distance)]) + sum(distance[0:destination]), sum(distance[destination:start]))