class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = s[0]
        longest_length = 1

        for i in range(length):
            # Assume the center is a character
            left = i
            right = i

            # Expand from the center until the characters are different
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            # If the length of the palindrome is longer than the previous one, update the longest palindrome
            if right - left - 1 > longest_length:
                longest = s[left + 1:right]
                longest_length = right - left - 1

            # Assume the center is between two characters
            # Repeat the same process as above
            left = i
            right = i + 1

            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > longest_length:
                longest = s[left + 1:right]
                longest_length = right - left - 1

        return longest
