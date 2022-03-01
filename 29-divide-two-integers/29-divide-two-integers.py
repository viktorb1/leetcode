class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        while divisor <= dividend:
            sum_of_divisors = divisor
            num_divisors_added = 1
            
            while sum_of_divisors + sum_of_divisors <= dividend:
                sum_of_divisors += sum_of_divisors
                num_divisors_added += num_divisors_added
            
            dividend -= sum_of_divisors
            quotient += num_divisors_added
        
        if is_negative:
            return -min(2**31, quotient)
        else:
            return min(2**31 - 1, quotient)
            