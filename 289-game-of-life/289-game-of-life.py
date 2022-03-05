class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
                
                count = 0
                for x, y in neighbors:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] % 2:
                        count += 1
                
                if board[i][j] and (count < 2 or count > 3):
                    board[i][j] = 3 # 0 -> 2 alive
                elif not board[i][j] and count == 3:
                    board[i][j] = 2 # 1 -> 3 died
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0