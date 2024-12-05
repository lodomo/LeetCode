class Solution:
    def canChange(self, start: str, target: str) -> bool:
        stripped_start = start.replace('_', '')
        stripped_target = target.replace('_', '')
        if stripped_start != stripped_target:
            return False

        chars = len(stripped_start)
        n = len(start)
        startIndex = 0
        endIndex = 0

        for startIndex in range(n):
            if start[startIndex] == '_':
                continue
            else:
                chars -= 1

            while endIndex < n and target[endIndex] == '_':
                endIndex += 1

            if start[startIndex] != target[endIndex]:
                return False

            if startIndex < endIndex and start[startIndex] == 'L':
                return False

            if startIndex > endIndex and start[startIndex] == 'R':
                return False

            endIndex += 1
        return True

