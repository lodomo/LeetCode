class Solution:
    def maximumLength(self, s: str) -> int:
        s = s + "~"
        strlen = len(s)
        letterCounts = {}
        prevLetter = None

        prevLetter = s[0]
        count = 1

        for i in range(1, strlen):
            if s[i] == prevLetter:
                count += 1
                continue

            count_balance = 1
            while count > 0:
                if prevLetter not in letterCounts:
                    letterCounts[prevLetter] = {}
                self.addToDictSum(letterCounts[prevLetter], count, count_balance)
                count_balance += 1
                count -= 1

            count = 1
            prevLetter = s[i]

        result = -1
        for key in letterCounts:
            for lengths in letterCounts[key]:
                if letterCounts[key][lengths] >= 3:
                    result = max(result, lengths)

        return result

    def addToDictSum(self, dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = 0
        dictionary[key] += value




cases = ["aaaa", "abcdef", "abcaba"]

for case in cases:
    print(Solution().maximumLength(case))
