import numpy as np


class List(list):
    pass


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solver = SudokuSolver(board)
        solved = solver.solve()
        self.updateBoardFromGrid(board, solved)
        return None

    def updateBoardFromGrid(self, board, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    board[i][j] = str(grid[i][j])


class SudokuSolver:
    width = 9
    height = 9
    squares = 9
    total_cells = 81
    default_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, board: list):
        self.rows = [set() for _ in range(SudokuSolver.height)]
        self.cols = [set() for _ in range(SudokuSolver.width)]
        self.sqrs = [set() for _ in range(SudokuSolver.squares)]
        self.candidates = [
            [set() for _ in range(SudokuSolver.width)]
            for _ in range(SudokuSolver.height)
        ]
        self.empty_cells = 81
        self.board = self.list_2D_to_np_array(board)
        self.initializeCandidates()

    def list_2D_to_np_array(self, board):
        grid = np.zeros((9, 9), dtype=int)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    grid[i][j] = int(board[i][j])
        return grid

    def initializeCandidates(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    self.candidates[row][col] = self.default_set
                else:
                    self.rows[row].add(self.board[row][col])
                    self.cols[col].add(self.board[row][col])
                    self.sqrs[self.getSquare(row, col)].add(
                        self.board[row][col])
                    self.empty_cells -= 1
        self.updateCandidates()

    def getSquare(self, row, col):
        return (row // 3) * 3 + col // 3

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
            print(" ".join(map(str, p)))
            if i % 3 == 2:
                print("-------------------------")
        print(f"Empty Cells: {self.empty_cells}")
        print(f"Filled Cells: {self.total_cells - self.empty_cells}")

    def printCandidates(self):
        # Create an empty 27x27 grid for the output
        output = [[" " for _ in range(27)] for _ in range(27)]

        for row in range(9):
            for col in range(9):
                start_row, start_col = row * 3, col * 3

                if self.board[row][col] != 0:  # If the cell has a number
                    num = str(self.board[row][col])
                    output[start_row + 1][start_col + 1] = num
                else:  # If the cell is empty, print candidates
                    for candidate in self.candidates[row][col]:
                        # Map candidate numbers to positions in the 3x3 grid
                        candidate_row = (candidate - 1) // 3
                        candidate_col = (candidate - 1) % 3
                        output[start_row + candidate_row][start_col + candidate_col] = (
                            str(candidate)
                        )

        # Print the 27x27 grid with gridlines
        for i, line in enumerate(output):
            print(" ".join(line))

    def updateCandidates(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    self.candidates[row][col] = (
                        self.default_set
                        - self.rows[row]
                        - self.cols[col]
                        - self.sqrs[self.getSquare(row, col)]
                    )

    def soloCandidate(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col]:
                    continue

                if len(self.candidates[row][col]) == 1:
                    self.board[row][col] = self.candidates[row][col].pop()
                    self.rows[row].add(self.board[row][col])
                    self.cols[col].add(self.board[row][col])
                    self.sqrs[self.getSquare(row, col)].add(
                        self.board[row][col])
                    self.empty_cells -= 1
                    self.candidates[row][col] = set()

    def horizontalDiffs(self, row_y, col_x):
        this_set = self.candidates[row_y][col_x]
        dif_set = set()
        for col in range(9):
            if col == col_x:
                continue
            dif_set = dif_set.union(self.candidates[row_y][col])
        return this_set - dif_set

    def verticalDiffs(self, row_y, col_x):
        this_set = self.candidates[row_y][col_x]
        dif_set = set()
        for row in range(9):
            if row == row_y:
                continue
            dif_set = dif_set.union(self.candidates[row][col_x])
        return this_set - dif_set

    def squareDiffs(self, row_y, col_x):
        this_set = self.candidates[row_y][col_x]
        dif_set = set()
        for row in range(3):
            for col in range(3):
                if row == row_y and col == col_x:
                    continue
                dif_set = dif_set.union(
                    self.candidates[row_y - row_y % 3 + row][col_x - col_x % 3 + col]
                )
        return this_set - dif_set

    def horizontalWin(self):
        for col1 in range(9):
            for row in range(9):
                diff = self.horizontalDiffs(row, col1)
                if len(diff) == 1:
                    self.board[row][col1] = diff.pop()
                    self.rows[row].add(self.board[row][col1])
                    self.cols[col1].add(self.board[row][col1])
                    self.sqrs[self.getSquare(row, col1)].add(
                        self.board[row][col1])
                    self.empty_cells -= 1
                    self.candidates[row][col1] = set()

    def verticalWin(self):
        for row1 in range(9):
            for col in range(9):
                diff = self.verticalDiffs(row1, col)
                if len(diff) == 1:
                    self.board[row1][col] = diff.pop()
                    self.rows[row1].add(self.board[row1][col])
                    self.cols[col].add(self.board[row1][col])
                    self.sqrs[self.getSquare(row1, col)].add(
                        self.board[row1][col])
                    self.empty_cells -= 1
                    self.candidates[row1][col] = set()

    def squareWin(self):
        for square in range(9):
            for row in range(3):
                for col in range(3):
                    diff = self.squareDiffs(row, col)
                    if len(diff) == 1:
                        self.board[row][col] = diff.pop()
                        self.rows[row].add(self.board[row][col])
                        self.cols[col].add(self.board[row][col])
                        self.sqrs[self.getSquare(row, col)].add(
                            self.board[row][col])
                        self.empty_cells -= 1
                        self.candidates[row][col] = set()

    def isSameBoard(self, board1, board2):
        for i in range(9):
            for j in range(9):
                if board1[i][j] != board2[i][j]:
                    return False
        return True

    def solve(self):
        board_copy = None
        # print("Original")
        # self.printPretty(self.board)
        while (
            board_copy is None or not self.isSameBoard(self.board, board_copy)
        ) and self.empty_cells > 0:
            board_copy = np.copy(self.board)
            print("Solo Candidates")
            self.soloCandidate()
            self.updateCandidates()
            self.printPretty(self.board)

            print("Horizontal Scan")
            self.horizontalWin()
            self.updateCandidates()
            self.printPretty(self.board)

            print("Vertical Scan")
            self.verticalWin()
            self.printPretty(self.board)
            self.updateCandidates()

            print("Square Scan")
            self.squareWin()
            self.printPretty(self.board)
            self.updateCandidates()

        print("Candidates")
        self.printCandidates()

        return self.board


"""
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
"""

board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."],
]

Solution().solveSudoku(board)
