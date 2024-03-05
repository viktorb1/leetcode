class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])
        min_cost = float('inf')
        total_quality = 0
        max_heap = []

        for ratio, q in workers:
            total_quality += q
            heappush(max_heap, -q)

            if len(max_heap) > k:
                total_quality += heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * total_quality)

        return min_cost
