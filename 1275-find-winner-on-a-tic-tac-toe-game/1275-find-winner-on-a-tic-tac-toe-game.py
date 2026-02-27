class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        for i, move in enumerate(moves):
            row, col = move
            board[row][col] = 1 if i % 2 == 0 else -1
        for i in range(3):
            if sum(board[i]) == 3:
                return "A"
            if sum(board[i]) == -3:
                return "B"
        for j in range(3):
            if sum(board[i][j] for i in range(3)) == 3:
                return "A"
            if sum(board[i][j] for i in range(3)) == -3:
                return "B"
        if sum(board[i][i] for i in range(3)) == 3:
            return "A"
        if sum(board[i][i] for i in range(3)) == -3:
            return "B"

        if sum(board[i][2 - i] for i in range(3)) == 3:
            return "A"
        if sum(board[i][2 - i] for i in range(3)) == -3:
            return "B"

        return "Draw" if len(moves) == 9 else "Pending"  