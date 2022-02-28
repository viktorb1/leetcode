class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        
        for i, m in enumerate(reversed(num2)):
            carry = 0
            cur_num = ""
            
            for n in reversed(num1):
                mult = int(m) * int(n)
                rem = (mult + carry) % 10
                carry = (mult + carry) // 10
                cur_num = str(rem) + cur_num
            
            cur_num = str(carry) + cur_num
            total += int(cur_num) * pow(10, i)
        
        return str(total)