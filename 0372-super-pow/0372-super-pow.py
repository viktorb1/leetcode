class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1
        return (pow(self.superPow(a, b[:-1]), 10, 1337) * pow(a, b[-1], 1337)) % 1337