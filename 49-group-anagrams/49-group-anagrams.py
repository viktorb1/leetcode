class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            x[tuple(sorted(s))].append(s)

        return [l for l in x.values()]