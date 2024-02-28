import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parseEq(equation):
            x_sum, num_sum = 0, 0
            for section in equation.split('+'):
                split = section.split('-')
                x_diff, num_diff = add(split[0])
                x_sum += x_diff
                num_sum += num_diff

                for chunk in split[1:]:
                    x_diff, num_diff = add(chunk)
                    x_sum -= x_diff
                    num_sum -= num_diff
            
            return x_sum, num_sum
        
        def add(chunk, x_sum = 0, num_sum = 0):
            if chunk == "": return 0, 0
            try:
                return 0, int(chunk)
            except:
                try:
                    return int(chunk[:-1]), 0
                except:
                    return 1, 0
        
        
        left, right = equation.split('=')
        l_x_sum, l_num_sum = parseEq(left)
        r_x_sum, r_num_sum = parseEq(right)
        
        if l_x_sum == r_x_sum and l_num_sum == r_num_sum:
            return "Infinite solutions"
        elif l_x_sum == r_x_sum and l_num_sum != r_num_sum:
            return "No solution"
        elif l_num_sum == r_num_sum:
            return "x=0"
        else:
            return f'x={(r_num_sum - l_num_sum) // (l_x_sum - r_x_sum)}'