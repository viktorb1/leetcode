class Solution:
    def my_pow(self, n, p, _mod=1000000007):
        if p == 0: return 1
        z = self.my_pow(n, p//2)
        return (z * z * (n if p % 2 == 1 else 1)) % _mod

    def countGoodNumbers(self, n: int) -> int:
        return self.my_pow(5, (n+1)//2) * self.my_pow(4, n//2) % 1000000007

    
