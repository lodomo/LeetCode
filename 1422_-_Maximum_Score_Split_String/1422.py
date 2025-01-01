class Solution:
    def maxScore(self, s: str) -> int:
        str_len = len(s)
        ones = s.count('1')
        zeros = 0
        max_score = 0

        for i in range(str_len - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            max_score = max(max_score, zeros + ones)

        return max_score



