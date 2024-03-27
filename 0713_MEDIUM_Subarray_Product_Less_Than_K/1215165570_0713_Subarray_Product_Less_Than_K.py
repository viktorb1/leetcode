class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        q = deque()
        total = 0

        for n in nums:
            q.append(n)
            prod *= n
            while prod >= k and q:
                num = q.popleft()
                prod //= num
            total += len(q)
        
        return total
            