class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        
        for i, m in enumerate(reversed(num2)):
            carry = 0
            cur_prod = ""
            
            for n in reversed(num1):
                mult = int(m) * int(n)
                rem = (mult + carry) % 10
                carry = (mult + carry) // 10
                cur_prod = str(rem) + cur_prod
            
            cur_prod = str(carry) + cur_prod
            total += int(cur_prod) * pow(10, i)
        
        return str(total)