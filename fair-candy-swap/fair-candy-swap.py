class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceCount = sum(aliceSizes)
        bobCount = sum(bobSizes)
        alice = set()
        bob = set()
        
        for i in aliceSizes:
            alice.add(i)
            
        for i in bobSizes:
            bob.add(i)
        
        diff = (bobCount - aliceCount) // 2
        
        for i in alice:
            if i + diff in bob:
                return [i, i + diff]
