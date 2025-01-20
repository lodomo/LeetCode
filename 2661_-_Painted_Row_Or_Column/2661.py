class List(list):
    pass


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        arr_len = len(arr)

        row_count = [cols] * rows
        col_count = [rows] * cols

        row_map = {}
        col_map = {}

        for row in range(rows):
            for col in range(cols):
                row_map[mat[row][col]] = row
                col_map[mat[row][col]] = col

        for i in range(arr_len):
            row = row_map[arr[i]]
            col = col_map[arr[i]]

            row_count[row] -= 1
            col_count[col] -= 1

            if row_count[row] == 0 or col_count[col] == 0:
                return i

        return -1


arr = [1, 4, 5, 2, 6, 3]
mat = [[4, 3, 5], [1, 2, 6]]

s = Solution()
print(s.firstCompleteIndex(arr, mat))
