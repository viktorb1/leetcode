class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        for i in range(len(str2), 0, -1):
            if len(str2) % i != 0 or len(str1) % i != 0:
                continue
            
            for j in range(i, len(str2), i):
                if str2[j:j+i] != str2[:i]:
                    break;
            else:
                for j in range(0, len(str1), i):
                    if str1[j:j+i] != str2[:i]:
                        break
                    elif j == len(str1)-i:
                        return str2[:i]

        return ""
