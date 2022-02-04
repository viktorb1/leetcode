class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_letter(w, i, j):
            if not w:
                return True
            if not isInBounds(i, j) or board[i][j] != w[0]:
                return False

            board[i][j] = "#"
            
            for x, y in ((i, j+1), (i+1, j), (i-1, j), (i, j-1)):
                if search_letter(w[1:], x, y):
                    return True
            
            board[i][j] = w[0]
            return False
            
        def isInBounds(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search_letter(word, i, j):
                    return True