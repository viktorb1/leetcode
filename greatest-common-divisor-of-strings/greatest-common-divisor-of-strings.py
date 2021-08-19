class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pattern = ""
        shorter = str2 if len(str2) < len(str1) else str1
        longer = str2 if len(str2) >= len(str1) else str1
        
        for i in range(1, len(shorter) + 1):
            if len(shorter) % i != 0 or len(longer) % i != 0:
                continue
            
            for j in range(0, len(shorter), i):
                if shorter[j:j+i] != shorter[:i]:
                    break;
            else:
                for j in range(0, len(longer), i):
                    if longer[j:j+i] != shorter[:i]:
                        break
                    elif j == len(longer)-i:
                        pattern = shorter[:i]

        return pattern
