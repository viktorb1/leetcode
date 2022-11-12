class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        phi_1337 = 1140
        rem = int(''.join([str(i) for i in b])) % phi_1337
        return (a ** rem) % 1337