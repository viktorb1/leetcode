class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def keep(i, j, seen=set()):
            if board[i][j] == 'X' or board[i][j] == 'c':
                return
            elif board[i][j] == 'O':
                board[i][j] = 'c'
            
            seen.add((i, j))
            
            for (x,y) in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in seen:
                    keep(x, y, seen)
            
            seen.discard((i,j))
    
        for i in range(len(board[0])):
            keep(0, i)
            keep(len(board)-1, i)

        for i in range(len(board)):
            keep(i, 0)
            keep(i, len(board[0])-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'c':
                    board[i][j] = 'O'
            