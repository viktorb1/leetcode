class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        
        for c, v in count.items():
            max_in_a_group = c + 1
            groups = ceil(v / max_in_a_group)
            total += max_in_a_group*groups
        
        return total