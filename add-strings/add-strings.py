class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = "0" * max(len(num2) - len(num1), 0) + num1
        num2 = "0" * max(len(num1) - len(num2), 0) + num2
        ans = deque([])
        
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            c1, c2 = ord(num1[i]) - ord('0'), ord(num2[i]) - ord('0')
            total = (c1 + c2 + carry) % 10
            ans.appendleft(str(total))
            carry = (c1 + c2 + carry) // 10
        
        return ''.join(ans) if not carry else '1' + ''.join(ans)