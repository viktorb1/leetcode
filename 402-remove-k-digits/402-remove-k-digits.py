class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        
        while k > 0:
            for i in range(len(num)-1):
                if num[i] > num[i+1] and k > 0:
                    num.pop(i)
                    k-= 1
                    break
            else:
                num.pop(-1)
                k -= 1

        return str(int(''.join(num))) if num else "0"