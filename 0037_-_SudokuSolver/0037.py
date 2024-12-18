import numpy as np


class List(list):
    pass


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        cans = [[List() for _ in range(9)] for _ in range(9)]

        # Create a 9x9 numpy array
        grid = np.zeros((9, 9), dtype=int)
        self.updateGridFromBoard(grid, board)

        self.printPretty(board)
        self.printPretty(grid)

        self.updateBoardFromGrid(board, grid)
        return None

    def printPretty(self, board):
        print("-------------------------")
        for i in range(9):
            p = ["|"]
            for j in range(9):
                if board[i][j] == "." or board[i][j] == 0:
                    p.append(" ")
                else:
                    p.append(board[i][j])
                if j % 3 == 2:
                    p.append("|")
            print(' '.join(map(str, p)))
            if i % 3 == 2:
                print("-------------------------")

    def updateBoardFromGrid(self, board, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    board[i][j] = str(grid[i][j])

    def updateGridFromBoard(self, grid, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    grid[i][j] = int(board[i][j])


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(Solution().solveSudoku(board))
