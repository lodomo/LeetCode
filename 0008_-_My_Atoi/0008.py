class Solution:
    def myAtoi(self, s: str) -> int:
        strlen = len(s)
        sign = 1
        start = 0
        signed = False
        while start < strlen:
            if s[start].isdigit():
                break

            if signed and not s[start].isdigit():
                return 0

            if s[start] == "-":
                sign = -1
                signed = True
            elif s[start] == "+":
                signed = True
                sign = 1
            elif s[start] != " " and s[start] != "0":
                return 0

            start += 1

        end = start
        while end < strlen:
            if not s[end].isdigit():
                break
            end += 1

        if start == end:
            return 0

        MIN = -2**31
        MAX = 2**31 - 1
        VAL = int(s[start:end]) * sign

        return min(max(VAL, MIN), MAX)

s = "words and 987"

print(Solution().myAtoi(s))
