class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0 
        
        while i < len(data):
            if bin(data[i])[2:].zfill(8)[:1] == '0':
                i += 1
            elif bin(data[i])[2:].zfill(8)[:3] == '110':
                if len(data[i:]) < 2:
                    return False
                elif bin(data[i+1])[2:].zfill(8)[:2] != '10':
                    return False
                i += 2
            elif bin(data[i])[2:].zfill(8)[:4] == '1110':
                if len(data[i:]) < 3:
                    return False
                elif set([bin(data[i+1])[2:].zfill(8)[:2], bin(data[i+2])[2:].zfill(8)[:2]]) != {'10'}:
                    return False
                i += 3
            elif bin(data[i])[2:].zfill(8)[:5] == '11110':
                if len(data[i:]) < 4:
                    return False
                elif set([bin(data[i+1])[2:].zfill(8)[:2], bin(data[i+2])[2:].zfill(8)[:2], bin(data[i+3])[2:].zfill(8)[:2]]) != {'10'}:
                    return False
                i += 4
            else:
                return False
        
        return True