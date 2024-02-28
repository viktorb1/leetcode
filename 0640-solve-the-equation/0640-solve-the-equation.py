class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_eq(equation):
            sums = [0, 0] # x_sum, number_sum 
            for section in equation.split('+'):
                split = section.split('-')
                update_totals(split[0], sums, 1)
                for chunk in split[1:]:
                    update_totals(chunk, sums, -1)
            return sums
        
        def update_totals(chunk, sums, sign):
            if chunk.isdigit(): # chunk is a number
                sums[1] += sign*int(chunk)
            elif chunk[:-1].isdigit(): # chunk is a variable
                sums[0] += sign*int(chunk[:-1])
            elif chunk: # chunk is a variable with a '1'
                sums[0] += sign*1
        
        left, right = equation.split('=')
        l_x_sum, l_num_sum = parse_eq(left)
        r_x_sum, r_num_sum = parse_eq(right)
        
        if l_x_sum == r_x_sum and l_num_sum == r_num_sum:
            return "Infinite solutions"
        elif l_x_sum == r_x_sum and l_num_sum != r_num_sum:
            return "No solution"
        elif l_num_sum == r_num_sum:
            return "x=0"
        else:
            return f'x={(r_num_sum - l_num_sum) // (l_x_sum - r_x_sum)}'