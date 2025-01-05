class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_last = {}
        result = 0

        for i, c in enumerate(s):
            if c not in first_last:
                first_last[c] = [i, 0]
            first_last[c][1] = i

        for c in first_last:
            left, right = first_last[c]
            result += len(set(s[left+1:right]))

        return result

s = "aabca"
print(Solution().countPalindromicSubsequence(s)) # 3
