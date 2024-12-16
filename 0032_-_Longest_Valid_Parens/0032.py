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

        s = s[newStart:newEnd + 1]
        strlen = len(s)
        stack = []
        L = -1
        R = -2
        for i in range(strlen):
            if s[i] == "(":
                stack.append(L)
                continue

            if len(stack) == 0:
                continue

            if stack[-1] == L:
                stack.pop()
                stack.append(2)
                continue

            if stack[-1] == R:
                stack.append(R)
                continue

            if len(stack) > 1 and stack[-1] > 0:
                if stack[-2] == L:
                    current = stack.pop()
                    stack.pop()
                    stack.append(current + 2)
                    continue

                if stack[-2] == R:
                    stack.append(R)
                    continue

        print(stack)

        running_total = 0
        max_total = 0
        stack_len = len(stack)
        for i in range(stack_len):
            if stack[i] == L or stack[i] == R:
                max_total = max(max_total, running_total)
                running_total = 0
                continue

            running_total += stack[i]
        max_total = max(max_total, running_total)

        return max_total


case1 = "(()"
case2 = ")()())"
case3 = ""
case4 = "()(())"
caseMy = "((((((("
caseMy2 = ")))))))"
caseMy3 = "))))))()(((((("

cases = [case1, case2, case3, case4, caseMy, caseMy2, caseMy3]

for case in cases:
    print(f"Running case: {case}")
    print(Solution().longestValidParentheses(case))
