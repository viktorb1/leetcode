class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sols = set()
        enc = set()

        for i in range(len(s)-9):
            if s[i:i+10] in enc:
                sols.add(s[i:i+10])
            else:
                enc.add(s[i:i+10])
                
        return sols