class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        times_seen = Counter(arr).values()
        return len(times_seen) == len(set(times_seen))