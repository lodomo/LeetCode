import re


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        strlen = len(s)
        newStart = 0
        newEnd = strlen - 1
        while newStart < newEnd:
            if s[newStart] != "(":
                newStart += 1
                continue
            break

        while newEnd > newStart:
            if s[newEnd] != ")":
                newEnd -= 1
                continue
            break

        if newStart >= newEnd:
            return 0

        s = list(s[newStart: newEnd + 1])
        strlen = len(s)

        # Step 1: Find a () pair there must be atleast 1.
        for i in range(strlen - 1):
            if s[i] == "(" and s[i + 1] == ")":
                s[i] = 1
                s[i + 1] = 1
                left = self.pairLeft(i - 1, s, 0)
                right = self.pairRight(i + 2, s, strlen - 1)
                self.surrounded(left, right, s, strlen - 1)
                continue

        # Step 2: Find the longest sequence of 1's
        maxCount = 0
        count = 0
        for i in range(strlen):
            if s[i] == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        print(s)
        return max(maxCount, count)

    def pairRight(self, index, parenList, maxIndex):
        """
        If the index is a "(" and ")", then turn them into 1's,
        and keep looking right.

        if the index is not a pair, then return the index.
        """
        if index + 1 > maxIndex:
            return index

        if parenList[index] == "(" and parenList[index + 1] == ")":
            parenList[index] = 1
            parenList[index + 1] = 1
            return self.pairRight(index + 2, parenList, maxIndex)

        return index

    def pairLeft(self, index, parenList, minIndex):
        """
        If the index is a "(" and ")", then turn them into 1's,
        and keep looking left.
        """
        if index - 1 < minIndex:
            return index

        if parenList[index] == ")" and parenList[index - 1] == "(":
            parenList[index] = 1
            parenList[index - 1] = 1
            return self.pairLeft(index - 2, parenList)

        return index

    def surrounded(self, left, right, parenList, maxIndex):
        """
        If the left and right are a pair, then turn them into 1's.
        """
        while left > 0 and parenList[left] == 1:
            left -= 1

        while right < maxIndex and parenList[right] == 1:
            right += 1

        if left < 0 or right > maxIndex:
            return

        if parenList[left] == "(" and parenList[right] == ")":
            parenList[left] = 1
            parenList[right] = 1
            return self.surrounded(left - 1, right + 1, parenList, maxIndex)
        return


case1 = "(()"
case2 = ")()())"
case3 = ""
case4 = "()(())"
case5 = ")(((((()())()()))()(()))("
caseMy = "((((((("
caseMy2 = ")))))))"
caseMy3 = "))))))()(((((("


"""
cases = [case1, case2, case3, case4, caseMy, caseMy2, caseMy3]

for case in cases:
    print(f"Running case: {case}")
    print(Solution().longestValidParentheses(case))
"""
print(f"Running case: {case5}")
print(Solution().longestValidParentheses(case5))
