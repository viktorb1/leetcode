class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return sorted(c.keys(), key=lambda d: (-c.get(d), d))[:k]
