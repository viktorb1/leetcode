class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        v1 += [0] * (len(v2)-len(v1))
        v2 += [0] * (len(v1)-len(v2))
        
        for x, y in zip(v1, v2):
            if x < y:
                return -1
            elif x > y:
                return 1
        
        return 0