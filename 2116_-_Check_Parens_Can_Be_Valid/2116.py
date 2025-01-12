class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        opens = []
        wilds = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                wilds.append(i)
            elif c == '(':
                opens.append(i)
            elif opens:
                opens.pop()
            elif wilds:
                wilds.pop()
            else:
                return False

        while opens:
            if not wilds:
                return False

            if opens.pop() > wilds.pop():
                return False

        if len(wilds) % 2:
            return False

        return True


sol = Solution()
s = "()))(()(()()()()(((())())((()((())"
locked = "1100000000000010000100001000001101"

print(sol.canBeValid(s, locked))
