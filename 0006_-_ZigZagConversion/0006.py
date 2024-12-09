class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strlen = len(s)

        if strlen <= numRows or numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        j = 0
        i = 0
        direction = 1
        for i in range(strlen):
            rows[j].append(s[i])
            j += direction
            if j == numRows - 1:
                direction = -direction
            elif j == 0:
                direction = -direction

        flatten = []
        for row in rows:
            flatten.extend(row)

        return "".join(flatten)


s = "PAYPALISHIRING"
numRows = 3

print(Solution().convert(s, numRows))  # "PAHNAPLSIIGYIR"
