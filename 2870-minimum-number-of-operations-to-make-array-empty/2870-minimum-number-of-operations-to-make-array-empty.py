class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ops = 0
        
        for num, c in count.items():
            while c:
                if c == 4:
                    ops += 2
                    c -= 4
                elif c >= 3:
                    c -= 3
                    ops += 1
                elif c >= 2:
                    c -= 2
                    ops += 1
                else:
                    return -1
        
        return ops