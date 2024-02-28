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
                print(split)
                if len(split) > 1: 
                    for s in split[1:]:
                        x_diff, num_diff = add(s)
                        x_sum -= x_diff
                        num_sum -= num_diff
            
            return x_sum, num_sum
        
        def add(split, num_sum=0, x_sum=0):
            if split == "": return 0, 0
            try:
                num_sum = int(split)
            except:
                try:
                    x_sum = int(split[:-1])
                except:
                    x_sum = 1
            return x_sum, num_sum
        
        
        left, right = equation.split('=')
        l_x_sum, l_num_sum = parseEq(left)
        r_x_sum, r_num_sum = parseEq(right)
        print(l_x_sum, l_num_sum)
        print(r_x_sum, r_num_sum)
        
        if l_x_sum == r_x_sum and l_num_sum == r_num_sum:
            return "Infinite solutions"
        elif l_x_sum == r_x_sum and l_num_sum != r_num_sum:
            return "No solution"
        elif l_num_sum == r_num_sum:
            return "x=0"
        else:
            return f'x={(r_num_sum - l_num_sum) // (l_x_sum - r_x_sum)}'
    