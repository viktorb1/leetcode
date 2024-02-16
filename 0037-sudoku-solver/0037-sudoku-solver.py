class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.solve()
    
    def findUnassigned(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '.':
                    return (i, j)
        return (-1, -1)
    
    def solve(self):
        r, c = self.findUnassigned()
        if (r, c) == (-1, -1): return True
        
        for num in ['1','2', '3', '4', '5', '6', '7', '8', '9']:
            self.board[r][c] = num
            if self.checkValid(r,c):
                if self.solve():
                    return True
            
            self.board[r][c] = '.'
    
    
    def checkValid(self, r, c):
        br = r - r % 3
        bc = c - c % 3
        val = self.board[r][c]
        return self.check3by3(br, bc, val) and self.checkrow(r, val) and self.checkcol(c, val)

    def check3by3(self, br, bc, val):
        count = 0
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if self.board[i][j] == val:
                    count += 1
        return count == 1

    def checkrow(self, r, val):
        count = 0
        for c in range(9):
            if self.board[r][c] == val:
                count += 1
        return count == 1
    
    
    def checkcol(self, c, val):
        count = 0
        for r in range(9):
            if self.board[r][c] == val:
                count += 1
        return count == 1