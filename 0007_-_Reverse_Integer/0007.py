class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x < 0:
            reverse = -int(str(-x)[::-1])
        else:
            reverse = int(str(x)[::-1])

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse
