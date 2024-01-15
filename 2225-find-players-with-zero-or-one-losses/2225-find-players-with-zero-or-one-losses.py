class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_list = [l for _, l in matches]
        losers_counter = Counter(losers_list)
        winners = set([w for w, _ in matches])
        
        ans_1 = sorted(list(winners - losers_counter.keys()))
        ans_2 = sorted([l for l, c in losers_counter.items() if c == 1])

        return [ans_1, ans_2]