class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        sqr = {}

        for i in range(9):
            row[i] = set()
            col[i] = set()
            sqr[i] = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                num = board[r][c]

                if num in row[r]:
                    return False

                if num in col[c]:
                    return False

                sqr_index = (r // 3) * 3 + c // 3
                if num in sqr[sqr_index]:
                    return False

                col[c].add(num)
                row[r].add(num)
                sqr[sqr_index].add(num)

        return True
