class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        pair = []
        temp = []
        for char in s:
            if char == '(':
                stack.append(char)
                continue

            if not stack:
                pair = pair + temp
                pair.append(0)
                continue

            stack.pop()
            temp.append(1)

        if stack:
            pair.append(0)
        pair = pair + temp

        # Now we have a list of 1s and 0s
        # We want to find the longest contiguous sequence of 1s
        max_found = 0
        count = 0
        for p in pair:
            if p == 1:
                count += 1
            else:
                max_found = max(max_found, count)
                count = 0

        return max(max_found * 2, count * 2)
