class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)
        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            num_quotients_added = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                num_quotients_added += num_quotients_added
            dividend -= the_sum
            the_sum = divisor
            quotient += num_quotients_added

        if is_negative:
            return -min(quotient, 2**31)
        else:
            return min(quotient, 2**31-1)