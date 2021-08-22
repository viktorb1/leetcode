class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        
        for idx, ele in enumerate(s):
            if ele not in mapping:
                if t[idx] in mapping.values():
                    return False
                else:
                    mapping[ele] = t[idx]
            elif mapping[ele] != t[idx]:
                return False
            
        
        return True