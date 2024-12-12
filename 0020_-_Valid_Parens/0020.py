class Solution:
    def isValid(self, s: str) -> bool:
        left = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        prev = []

        for c in s:
            if c in left:
                prev.append(c)
            else:
                if not prev or left[prev.pop()] != c:
                    return False

        return not len(prev)
