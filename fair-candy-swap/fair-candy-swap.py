class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceCount = 0
        bobCount = 0
        alice = collections.Counter()
        bob = collections.Counter()
        
        for i in aliceSizes:
            aliceCount += i
            alice[i] += 1
            
        for i in bobSizes:
            bobCount += i
            bob[i] += 1
        
        diff = (bobCount - aliceCount) // 2
        
        for i in alice:
            if i + diff in bob:
                return [i, i + diff]