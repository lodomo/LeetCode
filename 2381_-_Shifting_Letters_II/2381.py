class List(list):
    pass

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        strlen = len(s)
        s = list(s)
        shift_list = [0] * (strlen + 1)  # Use strlen + 1 to handle boundaries
        FORWARD = 1

        for start, end, direction in shifts:
            delta = 1 if direction == FORWARD else -1
            shift_list[start] += delta
            shift_list[end + 1] -= delta

        for i in range(1, strlen):
            shift_list[i] += shift_list[i - 1]

        for i in range(strlen):
            shift = shift_list[i] % 26
            s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))

        return ''.join(s)


s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

print(Solution().shiftingLetters(s, shifts))
