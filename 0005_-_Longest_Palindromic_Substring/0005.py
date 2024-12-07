class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        left = 0
        right = 0
        longest = 1
        found = s[0]
        current = 0

        while right < length:
            if s[left] == s[right]:
                if right == left:
                    current = 1
                    right += 1
                    continue
                elif right - left == 1:
                    current = 2
                    if current > longest:
                        longest = current

                else:
                    current += 2
                    if current > longest:
                        longest = current
                left -= 1
                if left < 0:
                    left = right
                    current = 0
                right += 1
            if s[left] != s[right]:
                if right - left == 1:
                    left -= 1
                else:
                    left = right
                    current = 0

        return longest

