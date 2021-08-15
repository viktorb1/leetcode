class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceCount = 0
        bobCount = 0
        alice = set()
        bob = set()
        
        for i in aliceSizes:
            aliceCount += i
            alice.add(i)
            
        for i in bobSizes:
            bobCount += i
            bob.add(i)
        
        diff = (bobCount - aliceCount) // 2
        
        for i in alice:
            if i + diff in bob:
                return [i, i + diff]
